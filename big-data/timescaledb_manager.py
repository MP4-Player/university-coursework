import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pg8000.dbapi as db_driver
from datetime import datetime, timedelta
import random
import time
import threading
import json

# Попытка импорта matplotlib
try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
except ImportError:
    messagebox.showerror("Ошибка", "Для работы гистограмм установите matplotlib:\npip install matplotlib")

# Конфигурация
DB_CONFIG = {
    "user": "postgres",
    "password": os.environ.get("PGPASSWORD", ""),  # Ваш пароль
    "host": "127.0.0.1",
    "port": 5433,
    "database": "postgres",
}

COLORS = {
    'bg': "#50402C",
    'fg': "#B3DFEB",
    'btn': "#5E4F34",
    'btn_hover': "#2A1406",
    'accent': "#FF9436",
    'success': "#3AFF8C",
    'danger': "#FF4F3B",
    'log_bg': "#111D2C",
    'log_fg': '#00FF00',
    'listbox_bg': "#5E4A34",
    'listbox_fg': "#9DDAE9"
}

class TimescaleLabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лаб 8: TimescaleDB Manager")
        self.root.geometry("1200x850")
        self.root.configure(bg=COLORS['bg'])
        
        self.conn = None
        self.setup_ui()
        
    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background=COLORS['listbox_bg'], 
                        foreground=COLORS['listbox_fg'], fieldbackground=COLORS['listbox_bg'])
        style.configure("TLabel", background=COLORS['bg'], foreground=COLORS['fg'])
        style.configure("TFrame", background=COLORS['bg'])
        
        # Заголовок
        header = tk.Frame(self.root, bg=COLORS['bg'])
        header.pack(fill=tk.X, pady=10, padx=10)
        tk.Label(header, text="LAB 8 (TimescaleDB)", 
                font=('Segoe UI', 16, 'bold'), bg=COLORS['bg'], fg=COLORS['accent']).pack(side=tk.LEFT)
        
        self.status_lbl = tk.Label(header, text="🔴 Не подключено", bg=COLORS['bg'], fg='#E74C3C', font=('Segoe UI', 10))
        self.status_lbl.pack(side=tk.RIGHT)

        # Вкладки
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        tab1 = tk.Frame(notebook, bg=COLORS['bg'])
        notebook.add(tab1, text="1. Настройка и Данные")
        self.init_tab_setup(tab1)
        
        tab2 = tk.Frame(notebook, bg=COLORS['bg'])
        notebook.add(tab2, text="2. Анализ и Оптимизация")
        self.init_tab_analysis(tab2)
        
        tab3 = tk.Frame(notebook, bg=COLORS['bg'])

        self.init_tab_api(tab3)

        # Лог
        log_frame = tk.LabelFrame(self.root, text="Системный журнал", bg=COLORS['bg'], fg=COLORS['fg'])
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.log_area = scrolledtext.ScrolledText(log_frame, height=8, bg=COLORS['log_bg'], fg=COLORS['log_fg'], font=('Consolas', 10))
        self.log_area.pack(fill=tk.BOTH, expand=True)

        self.connect_db()

    def init_tab_setup(self, parent):
        main_container = tk.Frame(parent, bg=COLORS['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # --- ЛЕВАЯ КОЛОНКА ---
        left_col = tk.Frame(main_container, bg=COLORS['bg'])
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # 1. Структура БД
        step1 = tk.LabelFrame(left_col, text="Этап 1-3: Структура БД", bg=COLORS['bg'], fg=COLORS['fg'])
        step1.pack(fill=tk.X, pady=5)
        self.create_btn(step1, "Установить TimescaleDB + Таблицы по умолчанию", self.setup_database).pack(side=tk.LEFT, padx=5, pady=10)

        # 2. Генерация (ИЗМЕНЕНО: Выбор таблицы)
        step2 = tk.LabelFrame(left_col, text="Этап 4: Генерация данных", bg=COLORS['bg'], fg=COLORS['fg'])
        step2.pack(fill=tk.X, pady=10)
        
        tk.Label(step2, text="Кол-во:", bg=COLORS['bg'], fg=COLORS['fg']).pack(side=tk.LEFT, padx=5)
        self.count_var = tk.StringVar(value="10000")
        tk.Entry(step2, textvariable=self.count_var, width=8).pack(side=tk.LEFT)
        
        tk.Label(step2, text="В таблицу:", bg=COLORS['bg'], fg=COLORS['fg']).pack(side=tk.LEFT, padx=5)
        # Combobox для выбора таблицы при генерации
        self.gen_table_var = tk.StringVar()
        self.gen_table_combo = ttk.Combobox(step2, textvariable=self.gen_table_var, width=15, state="readonly")
        self.gen_table_combo.pack(side=tk.LEFT, padx=5)
        
        self.create_btn(step2, "🚀 Генерировать", self.generate_data).pack(side=tk.LEFT, padx=10, pady=10)

        # --- ПРАВАЯ КОЛОНКА (Список таблиц) ---
        right_col = tk.LabelFrame(main_container, text="Менеджер Таблиц", bg=COLORS['bg'], fg=COLORS['accent'])
        right_col.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))

        # Список
        list_frame = tk.Frame(right_col, bg=COLORS['bg'])
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.tables_listbox = tk.Listbox(list_frame, bg=COLORS['listbox_bg'], fg=COLORS['listbox_fg'], 
                                         selectbackground=COLORS['accent'], height=10)
        self.tables_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.tables_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        self.tables_listbox.config(yscrollcommand=scrollbar.set)

        # Кнопки управления
        btn_frame = tk.Frame(right_col, bg=COLORS['bg'])
        btn_frame.pack(fill=tk.X, padx=10, pady=10)

        self.create_btn(btn_frame, "🔄 Обновить список", self.load_tables).pack(fill=tk.X, pady=2)
        self.create_btn(btn_frame, "⚙️ Меню таблицы / Гистограмма", self.show_timescaledb_menu).pack(fill=tk.X, pady=2)
        self.create_btn(btn_frame, "➕ Создать новую таблицу", self.create_table).pack(fill=tk.X, pady=2)

    def init_tab_analysis(self, parent):
        frame = tk.Frame(parent, bg=COLORS['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Описание
        desc = "Сравнение производительности двух таблиц (AVG запрос за последние 7 дней)"
        tk.Label(frame, text=desc, bg=COLORS['bg'], fg=COLORS['fg'], font=('Segoe UI', 11)).pack(anchor='w', pady=(0, 15))
        
        # --- Блок выбора таблиц ---
        selection_frame = tk.LabelFrame(frame, text="Выбор таблиц для сравнения", bg=COLORS['bg'], fg=COLORS['fg'])
        selection_frame.pack(fill=tk.X, pady=10)
        
        # Таблица 1 (Обычно Plain)
        f1 = tk.Frame(selection_frame, bg=COLORS['bg'])
        f1.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
        tk.Label(f1, text="Таблица 1 (Стандартная):", bg=COLORS['bg'], fg='#ECF0F1').pack(anchor='w')
        self.analyze_t1_var = tk.StringVar()
        self.analyze_t1_combo = ttk.Combobox(f1, textvariable=self.analyze_t1_var, state="readonly")
        self.analyze_t1_combo.pack(fill=tk.X, pady=5)
        
        # Таблица 2 (Обычно Hypertable)
        f2 = tk.Frame(selection_frame, bg=COLORS['bg'])
        f2.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
        tk.Label(f2, text="Таблица 2 (Гипертаблица):", bg=COLORS['bg'], fg=COLORS['accent']).pack(anchor='w')
        self.analyze_t2_var = tk.StringVar()
        self.analyze_t2_combo = ttk.Combobox(f2, textvariable=self.analyze_t2_var, state="readonly")
        self.analyze_t2_combo.pack(fill=tk.X, pady=5)

        # --- Кнопки управления ---
        btn_frame = tk.Frame(frame, bg=COLORS['bg'])
        btn_frame.pack(fill=tk.X, pady=20)

        self.create_btn(btn_frame, "▶ Запустить сравнение скорости", self.run_performance_test).pack(anchor='w', pady=5)
        self.create_btn(btn_frame, "🔍 EXPLAIN ANALYZE (для Таблицы 2)", self.run_explain).pack(anchor='w', pady=5)
        
        tk.Label(btn_frame, text="* Тест предполагает наличие колонок 'time' и 'value'", 
                 bg=COLORS['bg'], fg='#7F8C8D', font=('Arial', 8)).pack(anchor='w')
        
    def init_tab_api(self, parent):
        frame = tk.Frame(parent, bg=COLORS['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        step6 = tk.LabelFrame(frame, text="Materialized Views", bg=COLORS['bg'], fg=COLORS['fg'])
        step6.pack(fill=tk.X, pady=5)
        self.create_btn(step6, "Создать View (Daily Avg)", self.create_materialized_view).pack(side=tk.LEFT, padx=10, pady=10)
        self.create_btn(step6, "Refresh View", self.refresh_view).pack(side=tk.LEFT, padx=10, pady=10)
        
        api_frame = tk.LabelFrame(frame, text="REST API Симуляция", bg=COLORS['bg'], fg=COLORS['fg'])
        api_frame.pack(fill=tk.X, pady=20)
        self.create_btn(api_frame, "🌍 Выполнить API запрос", self.simulate_api_call).pack(anchor='w', padx=10, pady=10)

    # ================= ЛОГИКА БД =================

    def connect_db(self):
        try:
            self.conn = db_driver.connect(**DB_CONFIG)
            self.conn.autocommit = True
            self.status_lbl.config(text="🟢 Подключено", fg=COLORS['success'])
            self.log("Успешное подключение к PostgreSQL")
            self.load_tables()
        except Exception as e:
            self.log(f"Ошибка подключения: {e}")
            messagebox.showerror("Error", f"Ошибка подключения:\n{e}")

    def load_tables(self):
        self.tables_listbox.delete(0, tk.END)
        # Очищаем комбобоксы
        self.gen_table_combo['values'] = []
        self.analyze_t1_combo['values'] = []
        self.analyze_t2_combo['values'] = []
        
        if not self.conn: return
        try:
            cur = self.conn.cursor()
            cur.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            rows = cur.fetchall()
            table_list = [row[0] for row in rows]
            
            # 1. Заполняем главный список
            for t in table_list:
                self.tables_listbox.insert(tk.END, t)
            
            # 2. Заполняем список генерации
            self.gen_table_combo['values'] = table_list
            if table_list:
                # Пытаемся выбрать sensors_hyper или первую
                if 'sensors_hyper' in table_list:
                    self.gen_table_combo.set('sensors_hyper')
                else:
                    self.gen_table_combo.set(table_list[0])
            
            # 3. Заполняем списки для анализа
            self.analyze_t1_combo['values'] = table_list
            self.analyze_t2_combo['values'] = table_list
            
            # Автовыбор для удобства
            if 'sensors_plain' in table_list:
                self.analyze_t1_combo.set('sensors_plain')
            elif table_list:
                self.analyze_t1_combo.set(table_list[0])
                
            if 'sensors_hyper' in table_list:
                self.analyze_t2_combo.set('sensors_hyper')
            elif len(table_list) > 1:
                self.analyze_t2_combo.set(table_list[1])
            
            self.log("Список таблиц обновлен.")
        except Exception as e:
            self.log(f"Ошибка загрузки таблиц: {e}")
    # ================= МЕНЮ TIMESCALE И ДЕЙСТВИЯ =================

    def show_timescaledb_menu(self):
        selection = self.tables_listbox.curselection()
        if not selection:
            messagebox.showwarning("Предупреждение", "Выберите таблицу из списка!")
            return
        
        table_name = self.tables_listbox.get(selection[0])
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Управление: {table_name}")
        dialog.geometry("600x600")
        dialog.configure(bg=COLORS['bg'])
        
        main_frame = tk.Frame(dialog, bg=COLORS['bg'], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(main_frame, text=f"Таблица: {table_name}", 
                 font=("Arial", 14, "bold"), bg=COLORS['bg'], fg=COLORS['accent']).pack(anchor=tk.W, pady=(0, 20))
        
        btn_opts = {'bg': COLORS['btn'], 'fg': COLORS['fg'], 'activebackground': COLORS['btn_hover'], 'relief': 'flat', 'font': ('Segoe UI', 10)}
        
        # 1. Timescale действия
        tk.Label(main_frame, text="TimescaleDB", bg=COLORS['bg'], fg='#95A5A6').pack(anchor=tk.W)
        tk.Button(main_frame, text="🔄 Преобразовать в гипертаблицу", 
                  command=lambda: self.convert_to_hypertable(table_name, dialog), **btn_opts).pack(fill=tk.X, pady=5)
        tk.Button(main_frame, text="📊 Инфо о гипертаблицах (Размер/Чанки)", 
                  command=lambda: self.show_hypertables_info(dialog), **btn_opts).pack(fill=tk.X, pady=5)
        
        # 2. Анализ
        tk.Label(main_frame, text="Анализ", bg=COLORS['bg'], fg='#95A5A6').pack(anchor=tk.W, pady=(10,0))
        tk.Button(main_frame, text="📈 Построить гистограмму (Выбор поля)", 
                  command=lambda: self.prepare_histogram(table_name), 
                  bg=COLORS['accent'], fg='white', font=('Segoe UI', 10, 'bold'), relief='flat').pack(fill=tk.X, pady=5)

        # 3. Опасная зона (Удаление)
        tk.Label(main_frame, text="Опасная зона", bg=COLORS['bg'], fg='#E74C3C').pack(anchor=tk.W, pady=(20,0))
        tk.Button(main_frame, text="🗑️ Удалить таблицу", 
                  command=lambda: self.delete_table(table_name, dialog), 
                  bg=COLORS['danger'], fg='white', font=('Segoe UI', 10, 'bold'), relief='flat').pack(fill=tk.X, pady=5)

        tk.Button(main_frame, text="❌ Закрыть", command=dialog.destroy, bg='#7F8C8D', fg='white', relief='flat').pack(pady=20)

    # --- УДАЛЕНИЕ ТАБЛИЦЫ ---
    def delete_table(self, table_name, dialog):
        if messagebox.askyesno("Подтверждение", f"Вы уверены, что хотите удалить таблицу '{table_name}'?\nЭто действие необратимо!"):
            try:
                cur = self.conn.cursor()
                cur.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
                self.log(f"Таблица {table_name} удалена.")
                messagebox.showinfo("Успех", f"Таблица {table_name} удалена.")
                dialog.destroy()
                self.load_tables()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось удалить: {e}")

    # --- ГИСТОГРАММА С ВЫБОРОМ ПОЛЯ ---
    def prepare_histogram(self, table_name):
        """1. Получаем список числовых полей"""
        try:
            cur = self.conn.cursor()
            # Ищем числовые колонки
            query = """
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = %s 
                AND data_type IN ('integer', 'bigint', 'smallint', 'double precision', 'real', 'numeric')
            """
            cur.execute(query, (table_name,))
            rows = cur.fetchall()
            numeric_cols = [r[0] for r in rows]
            
            if not numeric_cols:
                messagebox.showwarning("Внимание", "В этой таблице нет числовых полей для гистограммы.")
                return

            # 2. Диалог выбора поля
            self.show_column_selector(table_name, numeric_cols)
            
        except Exception as e:
            self.log(f"Ошибка анализа полей: {e}")

    def show_column_selector(self, table_name, columns):
        """2. Диалог выбора колонки"""
        diag = tk.Toplevel(self.root)
        diag.title("Выбор поля")
        diag.geometry("300x200")
        diag.configure(bg=COLORS['bg'])
        
        tk.Label(diag, text=f"Гистограмма для {table_name}", bg=COLORS['bg'], fg=COLORS['fg']).pack(pady=10)
        tk.Label(diag, text="Выберите поле:", bg=COLORS['bg'], fg=COLORS['fg']).pack()
        
        col_var = tk.StringVar(value=columns[0])
        cb = ttk.Combobox(diag, textvariable=col_var, values=columns, state="readonly")
        cb.pack(pady=5)
        
        def confirm():
            col = col_var.get()
            diag.destroy()
            self.show_histogram_plot(table_name, col)
            
        tk.Button(diag, text="Построить", command=confirm, bg=COLORS['success'], fg='white').pack(pady=20)

    def show_histogram_plot(self, table_name, column):
        """3. Построение графика"""
        self.log(f"Строим гистограмму: {table_name}.{column}")
        win = tk.Toplevel(self.root)
        win.title(f"Гистограмма: {column}")
        win.geometry("800x600")
        
        try:
            cur = self.conn.cursor()
            # Лимит точек для скорости отрисовки
            cur.execute(f"SELECT {column} FROM {table_name} WHERE {column} IS NOT NULL LIMIT 10000")
            data = [row[0] for row in cur.fetchall()]
            
            if not data:
                messagebox.showinfo("Инфо", "Данных нет.")
                win.destroy()
                return

            fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
            ax.hist(data, bins=30, color=COLORS['btn_hover'], edgecolor='black', alpha=0.7)
            ax.set_title(f"Распределение {column} ({table_name})")
            ax.set_xlabel(column)
            ax.set_ylabel("Частота")
            ax.grid(True, alpha=0.3)
            
            canvas = FigureCanvasTkAgg(fig, master=win)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка построения: {e}")

    # --- ГЕНЕРАЦИЯ ДАННЫХ ---
    def generate_data(self):
        target_table = self.gen_table_var.get()
        count = int(self.count_var.get())
        
        if not target_table:
            messagebox.showwarning("Ошибка", "Выберите таблицу для генерации!")
            return

        self.log(f"Генерация {count} строк в '{target_table}'...")
        
        def task():
            try:
                # Используем отдельное подключение для потока, чтобы избежать конфликтов
                t_conn = db_driver.connect(**DB_CONFIG)
                t_conn.autocommit = True # Важно для executemany в некоторых драйверах
                cur = t_conn.cursor()
                
                data = []
                start_time = datetime.now() - timedelta(days=30)
                
                # Подготовка данных (time, sensor_id, value)
                for i in range(count):
                    ts = start_time + timedelta(minutes=i)
                    sid = random.randint(1, 50)
                    val = random.uniform(20.0, 35.0)
                    data.append((ts, sid, val))
                
                t0 = time.time()
                
                # Попытка вставки. Предполагаем структуру (time, sensor_id, value)
                # Если таблица кастомная, это может упасть, но для sensors_* сработает
                query = f"INSERT INTO {target_table} (time, sensor_id, value) VALUES (%s, %s, %s)"
                
                # Для pg8000 используем цикл или executemany. 
                # executemany иногда дает "portal error" если autocommit включен странно.
                # Попробуем порциями (батчами)
                batch_size = 1000
                for i in range(0, len(data), batch_size):
                    batch = data[i:i + batch_size]
                    cur.executemany(query, batch)
                
                dur = time.time() - t0
                self.log(f"✅ Успешно вставлено {count} строк за {dur:.2f} сек")
                
                t_conn.close()
            except Exception as e:
                self.log(f"❌ Ошибка генерации: {e}")
                
        threading.Thread(target=task).start()

    # --- ИСПРАВЛЕННАЯ ИНФО О ГИПЕРТАБЛИЦАХ ---
    def show_hypertables_info(self, parent_dialog=None):
        if parent_dialog: parent_dialog.destroy()
        try:
            cur = self.conn.cursor()
            # Исправленный запрос: используем pg_total_relation_size вместо несуществующей колонки
            query = """
                SELECT 
                    hypertable_name, 
                    num_chunks, 
                    pg_size_pretty(pg_total_relation_size(format('%I.%I', hypertable_schema, hypertable_name)::regclass))
                FROM timescaledb_information.hypertables;
            """
            cur.execute(query)
            rows = cur.fetchall()
            
            win = tk.Toplevel(self.root)
            win.title("Hypertable Info")
            
            tree = ttk.Treeview(win, columns=("Name", "Chunks", "Total Size"), show="headings")
            tree.heading("Name", text="Имя")
            tree.heading("Chunks", text="Чанки")
            tree.heading("Total Size", text="Размер")
            tree.pack(fill=tk.BOTH, expand=True)
            
            if not rows:
                self.log("Гипертаблицы не найдены (или запрос пуст).")
            
            for r in rows:
                tree.insert("", tk.END, values=r)
        except Exception as e:
            self.log(f"Ошибка инфо: {e}")

    # --- СОЗДАНИЕ НОВОЙ ТАБЛИЦЫ ---
    def create_table(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Создание таблицы")
        dialog.geometry("400x500")
        dialog.configure(bg=COLORS['bg'])
        
        tk.Label(dialog, text="Имя таблицы:", bg=COLORS['bg'], fg=COLORS['fg']).pack(anchor='w', padx=10, pady=5)
        name_entry = tk.Entry(dialog)
        name_entry.pack(fill=tk.X, padx=10)
        
        fields_frame = tk.LabelFrame(dialog, text="Поля", bg=COLORS['bg'], fg=COLORS['fg'])
        fields_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.new_fields = []
        
        def add_field(def_name="", def_type="FLOAT"):
            f_row = tk.Frame(fields_frame, bg=COLORS['bg'])
            f_row.pack(fill=tk.X, pady=2)
            e_name = tk.Entry(f_row, width=15)
            e_name.pack(side=tk.LEFT, padx=2)
            e_name.insert(0, def_name)
            c_type = ttk.Combobox(f_row, values=["TIMESTAMPTZ", "FLOAT", "INTEGER", "TEXT"], width=12)
            c_type.pack(side=tk.LEFT, padx=2)
            c_type.set(def_type)
            self.new_fields.append((e_name, c_type))
        
        # Поля по умолчанию для совместимости с генератором
        add_field("time", "TIMESTAMPTZ")
        add_field("sensor_id", "INTEGER")
        add_field("value", "FLOAT")
        
        tk.Button(fields_frame, text="+ Поле", command=lambda: add_field("col", "FLOAT")).pack(pady=5)
        
        def do_create():
            tbl = name_entry.get()
            if not tbl: return
            cols = []
            for e, c in self.new_fields:
                cols.append(f"{e.get()} {c.get()}")
            
            sql = f"CREATE TABLE {tbl} ({', '.join(cols)});"
            try:
                cur = self.conn.cursor()
                cur.execute(sql)
                self.log(f"Таблица {tbl} создана.")
                self.load_tables()
                dialog.destroy()
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))

        tk.Button(dialog, text="Создать таблицу", command=do_create, bg=COLORS['success'], fg='white').pack(pady=10)

    # --- УТИЛИТЫ ---
    def convert_to_hypertable(self, table_name, parent_dialog):
        # ... (Код аналогичен предыдущему, но исправлен для pg8000)
        try:
            cur = self.conn.cursor()
            # Берем первую колонку типа TIMESTAMPTZ
            cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}' AND data_type LIKE '%timestamp%'")
            res = cur.fetchone()
            if not res:
                messagebox.showerror("Ошибка", "В таблице нет колонки timestamp/timestamptz!")
                return
            time_col = res[0]
            
            query = f"SELECT create_hypertable('{table_name}', '{time_col}', chunk_time_interval => interval '7 days', if_not_exists => TRUE);"
            cur.execute(query)
            self.log(f"Таблица {table_name} -> Hypertable.")
            messagebox.showinfo("Успех", "Преобразовано в гипертаблицу!")
            parent_dialog.destroy()
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def setup_database(self):
        def task():
            try:
                cur = self.conn.cursor()
                self.log("Настройка БД по умолчанию...")
                cur.execute("CREATE EXTENSION IF NOT EXISTS timescaledb;")
                cur.execute("DROP TABLE IF EXISTS sensors_plain CASCADE")
                cur.execute("CREATE TABLE sensors_plain (time TIMESTAMPTZ NOT NULL, sensor_id INT NOT NULL, value FLOAT NOT NULL);")
                cur.execute("DROP TABLE IF EXISTS sensors_hyper CASCADE")
                cur.execute("CREATE TABLE sensors_hyper (time TIMESTAMPTZ NOT NULL, sensor_id INT NOT NULL, value FLOAT NOT NULL);")
                cur.execute("SELECT create_hypertable('sensors_hyper', 'time', if_not_exists => TRUE);")
                self.log("✅ Готово.")
                self.root.after(0, self.load_tables)
            except Exception as e:
                self.log(f"❌ Ошибка: {e}")
        threading.Thread(target=task).start()
    
    # Старые методы (тесты, api) оставлены без изменений, но работают
    def run_performance_test(self):
        t1 = self.analyze_t1_var.get()
        t2 = self.analyze_t2_var.get()
        
        if not t1 or not t2:
            messagebox.showwarning("Ошибка", "Выберите обе таблицы для сравнения!")
            return

        self.log(f"\n--- ТЕСТ: {t1} vs {t2} ---")
        
        def task():
            try:
                cur = self.conn.cursor()
                
                # Тест Таблицы 1
                query1 = f"SELECT AVG(value) FROM {t1} WHERE time > NOW() - INTERVAL '7 days'"
                t0 = time.perf_counter()
                cur.execute(query1)
                cur.fetchall()
                dt1 = (time.perf_counter() - t0) * 1000
                self.log(f"1️⃣ {t1}: {dt1:.4f} ms")
                
                # Тест Таблицы 2
                query2 = f"SELECT AVG(value) FROM {t2} WHERE time > NOW() - INTERVAL '7 days'"
                t0 = time.perf_counter()
                cur.execute(query2)
                cur.fetchall()
                dt2 = (time.perf_counter() - t0) * 1000
                self.log(f"2️⃣ {t2}: {dt2:.4f} ms")
                
                # Итог
                if dt1 > dt2:
                    ratio = dt1 / dt2 if dt2 > 0 else 0
                    self.log(f"🏆 {t2} быстрее в {ratio:.1f} раз")
                elif dt2 > dt1:
                    ratio = dt2 / dt1 if dt1 > 0 else 0
                    self.log(f"🏆 {t1} быстрее в {ratio:.1f} раз")
                else:
                    self.log("Скорость одинакова.")
                    
            except Exception as e:
                self.log(f"❌ Ошибка теста (проверьте наличие колонок time/value): {e}")
                
        threading.Thread(target=task).start()

    def run_explain(self):
        target_table = self.analyze_t2_var.get()
        if not target_table:
            messagebox.showwarning("Ошибка", "Выберите 'Таблицу 2' для анализа запроса!")
            return
            
        query = f"EXPLAIN ANALYZE SELECT AVG(value) FROM {target_table} WHERE time > NOW() - INTERVAL '1 hour'"
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            result = "\n".join([r[0] for r in rows])
            
            win = tk.Toplevel(self.root)
            win.title(f"EXPLAIN ANALYZE: {target_table}")
            text = scrolledtext.ScrolledText(win, width=100, height=30, font=('Consolas', 9))
            text.pack(fill=tk.BOTH, expand=True)
            text.insert(tk.END, f"QUERY: {query}\n\n{result}")
        except Exception as e:
            self.log(f"Ошибка explain: {e}")
    def run_explain(self):
        try:
            cur = self.conn.cursor()
            cur.execute("EXPLAIN ANALYZE SELECT AVG(value) FROM sensors_hyper WHERE time > NOW() - INTERVAL '1 hour'")
            rows = cur.fetchall()
            res = "\n".join([r[0] for r in rows])
            win = tk.Toplevel(self.root)
            t = scrolledtext.ScrolledText(win, width=80)
            t.pack()
            t.insert(tk.END, res)
        except Exception as e:
            self.log(f"Explain Error: {e}")

    def create_materialized_view(self):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                CREATE MATERIALIZED VIEW IF NOT EXISTS sensors_daily_avg
                WITH (timescaledb.continuous) AS
                SELECT time_bucket('1 day', time) AS bucket, sensor_id, AVG(value) as avg_val
                FROM sensors_hyper GROUP BY bucket, sensor_id;
            """)
            self.log("View Created.")
        except Exception as e: self.log(str(e))

    def refresh_view(self):
        try:
            self.conn.cursor().execute("CALL refresh_continuous_aggregate('sensors_daily_avg', NULL, NULL);")
            self.log("View Refreshed.")
        except Exception as e: self.log(str(e))

    def simulate_api_call(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM sensors_daily_avg ORDER BY bucket DESC LIMIT 3")
            data = [{"time": str(r[0]), "id": r[1], "val": r[2]} for r in cur.fetchall()]
            win = tk.Toplevel(self.root)
            t = scrolledtext.ScrolledText(win)
            t.pack()
            t.insert(tk.END, json.dumps(data, indent=2))
        except Exception as e: messagebox.showerror("Err", str(e))

    def log(self, msg):
        ts = datetime.now().strftime('%H:%M:%S')
        self.log_area.insert(tk.END, f"[{ts}] {msg}\n")
        self.log_area.see(tk.END)

    def create_btn(self, parent, text, cmd):
        return tk.Button(parent, text=text, command=cmd, 
                       bg=COLORS['btn'], fg=COLORS['fg'], 
                       activebackground=COLORS['btn_hover'], activeforeground='white',
                       font=('Segoe UI', 9), relief='flat', padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimescaleLabApp(root)
    root.mainloop()