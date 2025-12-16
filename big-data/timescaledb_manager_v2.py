import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pg8000.dbapi as db_driver
from datetime import datetime, timedelta
import random
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import rcParams

# ================= ЧЕРНО-ОРАНЖЕВАЯ ПАЛИТРА =================
COLORS = {
    # Основные фоны
    'bg_dark': '#121212',           # Темный фон (основной)
    'bg_medium': '#1A1A1A',         # Средний фон
    'bg_light': '#222222',          # Светлый фон
    
    # Оранжевые акценты
    'orange_primary': '#FF5722',    # Основной оранжевый
    'orange_dark': '#E64A19',       # Темный оранжевый
    'orange_light': '#FF8A65',      # Светлый оранжевый
    'orange_accent': '#FF9800',     # Акцентный оранжевый
    
    # Серые оттенки
    'gray_dark': '#2C2C2C',         # Темно-серый
    'gray_medium': '#424242',       # Средне-серый
    'gray_light': '#616161',        # Светло-серый
    'gray_border': '#757575',       # Границы
    
    # Текст
    'text_primary': '#FFFFFF',      # Белый основной текст
    'text_secondary': '#B0B0B0',    # Серый вторичный текст
    'text_orange': '#FFAB40',       # Оранжевый текст
    
    # Статусы
    'success': '#4CAF50',           # Зеленый успех
    'warning': '#FFC107',           # Желтый предупреждение
    'error': '#F44336',             # Красный ошибка
    'info': '#2196F3',              # Синий информация
    
    # Кнопки
    'btn_orange': '#FF5722',        # Оранжевая кнопка
    'btn_orange_hover': '#FF7043',  # Оранжевая кнопка при наведении
    'btn_gray': '#424242',          # Серая кнопка
    'btn_gray_hover': '#616161',    # Серая кнопка при наведении
    
    # Ввод
    'input_bg': '#2C2C2C',          # Фон полей ввода
    'input_border': '#757575',      # Граница полей ввода
    'input_focus': '#FF5722',       # Фокус полей ввода
    
    # Списки
    'listbox_bg': '#1A1A1A',        # Фон списков
    'listbox_fg': '#FFFFFF',        # Текст списков
    'listbox_select': '#FF5722',    # Выделение в списке
    
    # Вкладки
    'tab_active': '#FF5722',        # Активная вкладка
    'tab_inactive': '#424242',      # Неактивная вкладка
    'tab_bg': '#1A1A1A',            # Фон вкладок
    
    # Лог
    'log_bg': '#0A0A0A',            # Фон лога
    'log_fg': '#FFA726',            # Текст лога (оранжевый)
    'log_success': '#81C784',       # Успешные сообщения
    'log_error': '#E57373',         # Ошибки в логе
}

# Настройка matplotlib для черно-оранжевой темы
rcParams.update({
    'figure.facecolor': COLORS['bg_dark'],
    'axes.facecolor': COLORS['bg_medium'],
    'axes.edgecolor': COLORS['gray_light'],
    'axes.labelcolor': COLORS['text_primary'],
    'axes.titlecolor': COLORS['orange_primary'],
    'text.color': COLORS['text_primary'],
    'xtick.color': COLORS['text_secondary'],
    'ytick.color': COLORS['text_secondary'],
    'grid.color': COLORS['gray_medium'],
    'grid.alpha': 0.3
})

# Конфигурация БД
DB_CONFIG = {
    "user": "postgres",
    "password": os.environ.get("PGPASSWORD", ""),
    "host": "127.0.0.1",
    "port": 5433,
    "database": "postgres",
}

class TimescaleLabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TimescaleDB Lab - Мониторинг данных")
        self.root.geometry("1200x850")
        self.root.configure(bg=COLORS['bg_dark'])
        
        # Центрирование окна
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        self.conn = None
        self.setup_ui()
        self.connect_db()
        
    def setup_ui(self):
        # Стилизация ttk
        style = ttk.Style()
        style.theme_use('clam')
        
        # Настройка стилей
        style.configure('TNotebook', background=COLORS['bg_dark'], borderwidth=0)
        style.configure('TNotebook.Tab', 
                       background=COLORS['tab_inactive'],
                       foreground=COLORS['text_primary'],
                       padding=[10, 5])
        style.map('TNotebook.Tab', 
                 background=[('selected', COLORS['tab_active'])],
                 foreground=[('selected', COLORS['text_primary'])])
        
        style.configure('TLabel', background=COLORS['bg_dark'], foreground=COLORS['text_primary'])
        style.configure('TFrame', background=COLORS['bg_dark'])
        style.configure('TLabelframe', background=COLORS['bg_dark'], foreground=COLORS['text_orange'])
        style.configure('TLabelframe.Label', background=COLORS['bg_dark'], foreground=COLORS['orange_primary'])
        
        # Заголовок
        header = tk.Frame(self.root, bg=COLORS['bg_dark'], height=60)
        header.pack(fill=tk.X, pady=(0, 10))
        header.pack_propagate(False)
        
        title_frame = tk.Frame(header, bg=COLORS['bg_dark'])
        title_frame.pack(side=tk.LEFT, padx=20)
        
        tk.Label(title_frame, text="TIMESCALE DB LAB", 
                font=('Segoe UI', 16, 'bold'), 
                bg=COLORS['bg_dark'], 
                fg=COLORS['orange_primary']).pack(side=tk.LEFT)
        
        tk.Label(title_frame, text="Мониторинг временных рядов", 
                font=('Segoe UI', 10), 
                bg=COLORS['bg_dark'], 
                fg=COLORS['text_secondary']).pack(side=tk.LEFT, padx=(10, 0))
        
        self.status_lbl = tk.Label(header, text="🔴 Нет подключения", 
                                  bg=COLORS['bg_dark'], 
                                  fg=COLORS['error'],
                                  font=('Segoe UI', 10, 'bold'))
        self.status_lbl.pack(side=tk.RIGHT, padx=20)
        
        # Вкладки
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 5))
        
        tab1 = tk.Frame(notebook, bg=COLORS['bg_dark'])
        notebook.add(tab1, text="🏗️  Управление данными")
        self.init_tab_setup(tab1)
        
        tab2 = tk.Frame(notebook, bg=COLORS['bg_dark'])
        notebook.add(tab2, text="📊 Анализ и оптимизация")
        self.init_tab_analysis(tab2)
        
        # Лог
        log_frame = tk.LabelFrame(self.root, text="Системный журнал", 
                                 bg=COLORS['bg_dark'], 
                                 fg=COLORS['orange_primary'],
                                 font=('Segoe UI', 10, 'bold'))
        log_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=(0, 10), height=150)
        
        self.log_area = scrolledtext.ScrolledText(log_frame, 
                                                 height=6, 
                                                 bg=COLORS['log_bg'], 
                                                 fg=COLORS['log_fg'],
                                                 font=('Consolas', 9),
                                                 insertbackground=COLORS['orange_primary'])
        self.log_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def init_tab_setup(self, parent):
        main_container = tk.Frame(parent, bg=COLORS['bg_dark'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # ЛЕВАЯ КОЛОНКА - Действия
        left_col = tk.LabelFrame(main_container, text="Действия", 
                                bg=COLORS['bg_dark'], 
                                fg=COLORS['orange_primary'])
        left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # 1. Структура БД
        step1_frame = tk.Frame(left_col, bg=COLORS['bg_dark'])
        step1_frame.pack(fill=tk.X, pady=10, padx=10)
        
        tk.Label(step1_frame, text="1. Инициализация БД", 
                bg=COLORS['bg_dark'], 
                fg=COLORS['text_primary'],
                font=('Segoe UI', 11, 'bold')).pack(anchor='w', pady=(0, 5))
        
        self.create_btn(step1_frame, "🔄 Установить TimescaleDB + таблицы", 
                       self.setup_database,
                       color='orange').pack(fill=tk.X, pady=2)
        
        # 2. Генерация данных
        step2_frame = tk.Frame(left_col, bg=COLORS['bg_dark'])
        step2_frame.pack(fill=tk.X, pady=10, padx=10)
        
        tk.Label(step2_frame, text="2. Генерация тестовых данных", 
                bg=COLORS['bg_dark'], 
                fg=COLORS['text_primary'],
                font=('Segoe UI', 11, 'bold')).pack(anchor='w', pady=(0, 5))
        
        gen_frame = tk.Frame(step2_frame, bg=COLORS['bg_dark'])
        gen_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(gen_frame, text="Количество:", 
                bg=COLORS['bg_dark'], fg=COLORS['text_secondary']).pack(side=tk.LEFT)
        
        self.count_var = tk.StringVar(value="10000")
        tk.Entry(gen_frame, textvariable=self.count_var, width=10,
                bg=COLORS['input_bg'], fg=COLORS['text_primary'],
                insertbackground=COLORS['orange_primary']).pack(side=tk.LEFT, padx=5)
        
        tk.Label(gen_frame, text="в таблицу:", 
                bg=COLORS['bg_dark'], fg=COLORS['text_secondary']).pack(side=tk.LEFT, padx=(10, 0))
        
        self.gen_table_var = tk.StringVar()
        self.gen_table_combo = ttk.Combobox(gen_frame, textvariable=self.gen_table_var, 
                                           width=15, state="readonly")
        self.gen_table_combo.pack(side=tk.LEFT, padx=5)
        
        self.create_btn(step2_frame, "🚀 Сгенерировать данные", 
                       self.generate_data,
                       color='orange').pack(fill=tk.X, pady=5)
        
        # ПРАВАЯ КОЛОНКА - Таблицы
        right_col = tk.LabelFrame(main_container, text="Управление таблицами", 
                                 bg=COLORS['bg_dark'], 
                                 fg=COLORS['orange_primary'])
        right_col.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Список таблиц
        list_frame = tk.Frame(right_col, bg=COLORS['bg_dark'])
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.tables_listbox = tk.Listbox(list_frame, 
                                        bg=COLORS['listbox_bg'], 
                                        fg=COLORS['listbox_fg'],
                                        selectbackground=COLORS['listbox_select'],
                                        selectforeground='white',
                                        font=('Consolas', 10))
        self.tables_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", 
                                command=self.tables_listbox.yview,
                                bg=COLORS['gray_medium'])
        scrollbar.pack(side=tk.RIGHT, fill="y")
        self.tables_listbox.config(yscrollcommand=scrollbar.set)
        
        # Кнопки управления таблицами
        btn_frame = tk.Frame(right_col, bg=COLORS['bg_dark'])
        btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        self.create_btn(btn_frame, "🔄 Обновить список", 
                       self.load_tables).pack(fill=tk.X, pady=2)
        self.create_btn(btn_frame, "⚙️  Действия с таблицей", 
                       self.show_timescaledb_menu, color='orange').pack(fill=tk.X, pady=2)
        self.create_btn(btn_frame, "➕ Создать новую таблицу", 
                       self.create_table).pack(fill=tk.X, pady=2)
        
    def init_tab_analysis(self, parent):
        frame = tk.Frame(parent, bg=COLORS['bg_dark'])
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(frame, text="Сравнение производительности таблиц", 
                bg=COLORS['bg_dark'], 
                fg=COLORS['orange_primary'],
                font=('Segoe UI', 12, 'bold')).pack(anchor='w', pady=(0, 20))
        
        # Выбор таблиц
        selection_frame = tk.LabelFrame(frame, text="Выбор таблиц для сравнения", 
                                       bg=COLORS['bg_dark'], 
                                       fg=COLORS['text_primary'])
        selection_frame.pack(fill=tk.X, pady=10)
        
        # Таблица 1
        f1 = tk.Frame(selection_frame, bg=COLORS['bg_dark'])
        f1.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
        
        tk.Label(f1, text="Стандартная таблица:", 
                bg=COLORS['bg_dark'], fg=COLORS['text_primary']).pack(anchor='w')
        
        self.analyze_t1_var = tk.StringVar()
        self.analyze_t1_combo = ttk.Combobox(f1, textvariable=self.analyze_t1_var, state="readonly")
        self.analyze_t1_combo.pack(fill=tk.X, pady=5)
        
        # Таблица 2
        f2 = tk.Frame(selection_frame, bg=COLORS['bg_dark'])
        f2.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
        
        tk.Label(f2, text="Гипертаблица:", 
                bg=COLORS['bg_dark'], fg=COLORS['orange_accent']).pack(anchor='w')
        
        self.analyze_t2_var = tk.StringVar()
        self.analyze_t2_combo = ttk.Combobox(f2, textvariable=self.analyze_t2_var, state="readonly")
        self.analyze_t2_combo.pack(fill=tk.X, pady=5)
        
        # Кнопки анализа
        btn_frame = tk.Frame(frame, bg=COLORS['bg_dark'])
        btn_frame.pack(fill=tk.X, pady=20)
        
        self.create_btn(btn_frame, "▶ Запустить сравнение скорости", 
                       self.run_performance_test, color='orange').pack(anchor='w', pady=5)
        self.create_btn(btn_frame, "🔍 EXPLAIN ANALYZE (гипертаблица)", 
                       self.run_explain).pack(anchor='w', pady=5)
        
        tk.Label(btn_frame, 
                text="* Для теста требуются колонки 'time' (timestamp) и 'value' (число)", 
                bg=COLORS['bg_dark'], fg=COLORS['text_secondary'], 
                font=('Arial', 8)).pack(anchor='w', pady=(10, 0))
        
    # ================= ПОДКЛЮЧЕНИЕ К БД =================
    
    def connect_db(self):
        try:
            self.conn = db_driver.connect(**DB_CONFIG)
            self.conn.autocommit = True
            self.status_lbl.config(text="🟢 Подключено", fg=COLORS['success'])
            self.log("Успешное подключение к PostgreSQL", 'success')
            self.load_tables()
        except Exception as e:
            self.log(f"Ошибка подключения: {e}", 'error')
            messagebox.showerror("Ошибка подключения", 
                                f"Не удалось подключиться к БД:\n\n{e}\n\n"
                                f"Проверьте:\n"
                                f"1. Запущен ли контейнер\n"
                                f"2. Пароль и порт в настройках\n"
                                f"3. Доступность сервера")
    
    def load_tables(self):
        self.tables_listbox.delete(0, tk.END)
        self.gen_table_combo['values'] = []
        self.analyze_t1_combo['values'] = []
        self.analyze_t2_combo['values'] = []
        
        if not self.conn:
            return
            
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
            
            # Заполняем список таблиц
            for t in table_list:
                self.tables_listbox.insert(tk.END, t)
            
            # Заполняем combobox'ы
            self.gen_table_combo['values'] = table_list
            self.analyze_t1_combo['values'] = table_list
            self.analyze_t2_combo['values'] = table_list
            
            # Автовыбор
            if table_list:
                self.gen_table_combo.set(table_list[0])
                self.analyze_t1_combo.set(table_list[0])
                if len(table_list) > 1:
                    self.analyze_t2_combo.set(table_list[1])
                else:
                    self.analyze_t2_combo.set(table_list[0])
            
            self.log(f"Загружено таблиц: {len(table_list)}", 'success')
        except Exception as e:
            self.log(f"Ошибка загрузки таблиц: {e}", 'error')
    
    # ================= МЕНЮ ТАБЛИЦЫ =================
    
    def show_timescaledb_menu(self):
        selection = self.tables_listbox.curselection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите таблицу из списка!")
            return
            
        table_name = self.tables_listbox.get(selection[0])
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Действия: {table_name}")
        dialog.geometry("500x400")
        dialog.configure(bg=COLORS['bg_dark'])
        
        # Центрирование
        dialog.update_idletasks()
        width = dialog.winfo_width()
        height = dialog.winfo_height()
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
        
        main_frame = tk.Frame(dialog, bg=COLORS['bg_dark'], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(main_frame, text=table_name, 
                font=("Segoe UI", 14, "bold"), 
                bg=COLORS['bg_dark'], 
                fg=COLORS['orange_primary']).pack(anchor=tk.W, pady=(0, 20))
        
        # TimescaleDB действия
        tk.Label(main_frame, text="Преобразование в гипертаблицу", 
                bg=COLORS['bg_dark'], fg=COLORS['text_primary']).pack(anchor=tk.W, pady=(10, 5))
        
        self.create_btn(main_frame, "🔄 Преобразовать в гипертаблицу", 
                       lambda: self.convert_to_hypertable(table_name, dialog),
                       color='orange').pack(fill=tk.X, pady=5)
        
        self.create_btn(main_frame, "📊 Информация о гипертаблицах", 
                       lambda: self.show_hypertables_info(dialog)).pack(fill=tk.X, pady=5)
        
        # Анализ
        tk.Label(main_frame, text="Анализ данных", 
                bg=COLORS['bg_dark'], fg=COLORS['text_primary']).pack(anchor=tk.W, pady=(20, 5))
        
        self.create_btn(main_frame, "📈 Построить гистограмму", 
                       lambda: self.prepare_histogram(table_name),
                       color='orange').pack(fill=tk.X, pady=5)
        
        # Опасная зона
        tk.Label(main_frame, text="Опасные действия", 
                bg=COLORS['bg_dark'], fg=COLORS['error']).pack(anchor=tk.W, pady=(30, 5))
        
        self.create_btn(main_frame, "🗑️ Удалить таблицу", 
                       lambda: self.delete_table(table_name, dialog),
                       color='error').pack(fill=tk.X, pady=5)
        
        tk.Button(main_frame, text="✖ Закрыть", command=dialog.destroy,
                 bg=COLORS['gray_medium'], fg=COLORS['text_primary'],
                 activebackground=COLORS['gray_light'],
                 font=('Segoe UI', 10), relief='flat', padx=20, pady=10).pack(pady=20)
    
    # ================= ИСПРАВЛЕННЫЙ МЕТОД ДЛЯ ГИПЕРТАБЛИЦ =================
    
    def convert_to_hypertable(self, table_name, parent_dialog):
        try:
            cur = self.conn.cursor()
            
            # 1. Проверим, есть ли данные в таблице
            cur.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cur.fetchone()[0]
            
            migrate_option = "if_not_exists => true"
            
            if row_count > 0:
                # 2. Спросить пользователя, что делать с данными
                response = messagebox.askyesnocancel(
                    "Таблица содержит данные",
                    f"Таблица '{table_name}' содержит {row_count:,} записей.\n\n"
                    "Выберите действие:\n"
                    "• 'Да' - Преобразовать с данными (миграция)\n"
                    "• 'Нет' - Очистить таблицу и создать пустую гипертаблицу\n"
                    "• 'Отмена' - Отменить операцию"
                )
                
                if response is None:  # Отмена
                    return
                elif response:  # Да - преобразовать с данными
                    migrate_option = "migrate_data => true, if_not_exists => true"
                else:  # Нет - очистить таблицу
                    if messagebox.askyesno("Подтверждение", 
                                          f"Очистить таблицу '{table_name}'?\nВсе данные будут удалены!"):
                        cur.execute(f"TRUNCATE TABLE {table_name}")
                    else:
                        return
            
            # 3. Найти timestamp колонку
            cur.execute(f"""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = '{table_name}' 
                AND data_type IN ('timestamp with time zone', 'timestamp without time zone', 'timestamptz', 'timestamp')
                LIMIT 1
            """)
            
            res = cur.fetchone()
            if not res:
                messagebox.showerror("Ошибка", 
                                    "В таблице нет колонки типа timestamp/timestamptz!\n"
                                    "Гипертаблица требует колонку времени.")
                return
                
            time_col = res[0]
            
            # 4. Создать гипертаблицу
            query = f"""
                SELECT create_hypertable(
                    '{table_name}', 
                    '{time_col}', 
                    chunk_time_interval => interval '7 days',
                    {migrate_option}
                );
            """
            
            self.log(f"Создание гипертаблицы: {table_name}", 'info')
            cur.execute(query)
            
            # 5. Проверить результат
            cur.execute(f"""
                SELECT hypertable_name, num_chunks 
                FROM timescaledb_information.hypertables 
                WHERE hypertable_name = '{table_name}'
            """)
            
            result = cur.fetchone()
            if result:
                success_msg = f"Таблица '{table_name}' успешно преобразована в гипертаблицу!"
                if 'migrate_data' in migrate_option:
                    success_msg += f"\nДанные ({row_count:,} записей) мигрированы."
                messagebox.showinfo("Успех", success_msg)
                self.log(f"Таблица '{table_name}' преобразована в гипертаблицу", 'success')
            else:
                messagebox.showwarning("Внимание", 
                                      "Не удалось подтвердить создание гипертаблицы.\n"
                                      "Проверьте в списке гипертаблиц.")
            
            parent_dialog.destroy()
            
        except Exception as e:
            error_msg = str(e)
            if "already a hypertable" in error_msg.lower():
                messagebox.showinfo("Информация", 
                                   f"Таблица '{table_name}' уже является гипертаблицей.")
            elif "table is not empty" in error_msg.lower():
                messagebox.showerror("Ошибка", 
                                    "Таблица не пустая! Используйте 'migrate_data => true'.\n"
                                    "В меню выберите 'Преобразовать с данными'.")
            else:
                messagebox.showerror("Ошибка", f"Не удалось преобразовать:\n{error_msg}")
            self.log(f"Ошибка создания гипертаблицы: {e}", 'error')
    
    def delete_table(self, table_name, dialog):
        if messagebox.askyesno("Подтверждение удаления", 
                              f"Вы уверены, что хотите удалить таблицу '{table_name}'?\n"
                              "Это действие необратимо!"):
            try:
                cur = self.conn.cursor()
                cur.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
                self.log(f"Таблица {table_name} удалена", 'warning')
                messagebox.showinfo("Успех", f"Таблица {table_name} удалена.")
                dialog.destroy()
                self.load_tables()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось удалить: {e}")
    
    # ================= ГИСТОГРАММА =================
    
    def prepare_histogram(self, table_name):
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

            self.show_column_selector(table_name, numeric_cols)
            
        except Exception as e:
            self.log(f"Ошибка анализа полей: {e}", 'error')
    
    def show_column_selector(self, table_name, columns):
        diag = tk.Toplevel(self.root)
        diag.title("Выбор поля для гистограммы")
        diag.geometry("350x200")
        diag.configure(bg=COLORS['bg_dark'])
        
        # Центрирование
        diag.update_idletasks()
        width = diag.winfo_width()
        height = diag.winfo_height()
        x = (diag.winfo_screenwidth() // 2) - (width // 2)
        y = (diag.winfo_screenheight() // 2) - (height // 2)
        diag.geometry(f'{width}x{height}+{x}+{y}')
        
        tk.Label(diag, text=f"Гистограмма: {table_name}", 
                bg=COLORS['bg_dark'], 
                fg=COLORS['orange_primary'],
                font=('Segoe UI', 11, 'bold')).pack(pady=10)
        
        tk.Label(diag, text="Выберите числовое поле:", 
                bg=COLORS['bg_dark'], fg=COLORS['text_primary']).pack()
        
        col_var = tk.StringVar(value=columns[0])
        cb = ttk.Combobox(diag, textvariable=col_var, values=columns, state="readonly")
        cb.pack(pady=10, padx=20, fill=tk.X)
        
        def confirm():
            col = col_var.get()
            diag.destroy()
            self.show_histogram_plot(table_name, col)
            
        tk.Button(diag, text="Построить гистограмму", command=confirm,
                 bg=COLORS['orange_primary'], fg='white',
                 activebackground=COLORS['orange_dark'],
                 font=('Segoe UI', 10, 'bold'),
                 padx=20, pady=10).pack(pady=20)
    
    def show_histogram_plot(self, table_name, column):
        self.log(f"Построение гистограммы: {table_name}.{column}", 'info')
        
        win = tk.Toplevel(self.root)
        win.title(f"Гистограмма: {table_name}.{column}")
        win.geometry("800x600")
        win.configure(bg=COLORS['bg_dark'])
        
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT {column} FROM {table_name} WHERE {column} IS NOT NULL LIMIT 10000")
            data = [row[0] for row in cur.fetchall()]
            
            if not data:
                messagebox.showinfo("Инфо", "Нет данных для построения гистограммы.")
                win.destroy()
                return

            fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
            
            # Используем оранжевую цветовую схему
            n, bins, patches = ax.hist(data, bins=30, alpha=0.7, edgecolor=COLORS['gray_light'])
            
            # Градиент оранжевых цветов
            for i in range(len(patches)):
                patches[i].set_facecolor(plt.cm.Oranges(i / len(patches)))
            
            ax.set_title(f"Распределение значений: {column}", color=COLORS['orange_primary'], fontsize=14)
            ax.set_xlabel(column, color=COLORS['text_primary'])
            ax.set_ylabel("Частота", color=COLORS['text_primary'])
            ax.grid(True, alpha=0.3, color=COLORS['gray_medium'])
            
            # Статистика
            mean_val = sum(data) / len(data)
            ax.axvline(mean_val, color=COLORS['orange_accent'], linestyle='--', linewidth=2, label=f'Среднее: {mean_val:.2f}')
            ax.legend(facecolor=COLORS['bg_medium'], edgecolor=COLORS['gray_light'])
            
            canvas = FigureCanvasTkAgg(fig, master=win)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            # Кнопка сохранения
            btn_frame = tk.Frame(win, bg=COLORS['bg_dark'])
            btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
            
            tk.Button(btn_frame, text="Сохранить график", 
                     command=lambda: self.save_figure(fig, f"histogram_{table_name}_{column}"),
                     bg=COLORS['orange_primary'], fg='white',
                     padx=15, pady=5).pack(side=tk.RIGHT)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка построения гистограммы:\n{e}")
            win.destroy()
    
    def save_figure(self, fig, filename):
        try:
            fig.savefig(f"{filename}.png", dpi=300, bbox_inches='tight', 
                       facecolor=COLORS['bg_dark'])
            self.log(f"График сохранен: {filename}.png", 'success')
            messagebox.showinfo("Успех", f"График сохранен как {filename}.png")
        except Exception as e:
            self.log(f"Ошибка сохранения: {e}", 'error')
    
    # ================= ГЕНЕРАЦИЯ ДАННЫХ =================
    
    def generate_data(self):
        target_table = self.gen_table_var.get()
        try:
            count = int(self.count_var.get())
            if count <= 0:
                messagebox.showerror("Ошибка", "Количество должно быть положительным числом!")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число!")
            return
            
        if not target_table:
            messagebox.showwarning("Ошибка", "Выберите таблицу для генерации!")
            return

        self.log(f"Генерация {count:,} строк в '{target_table}'...", 'info')
        
        def task():
            try:
                # Используем отдельное подключение для потока
                t_conn = db_driver.connect(**DB_CONFIG)
                t_conn.autocommit = True
                cur = t_conn.cursor()
                
                data = []
                start_time = datetime.now() - timedelta(days=30)
                
                # Подготовка данных
                for i in range(count):
                    ts = start_time + timedelta(seconds=random.randint(0, 2592000))  # 30 дней в секундах
                    sid = random.randint(1, 50)
                    val = random.uniform(20.0, 35.0)
                    data.append((ts, sid, val))
                
                t0 = time.time()
                
                # Проверяем структуру таблицы
                cur.execute(f"""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = '{target_table}'
                    ORDER BY ordinal_position
                """)
                
                columns = cur.fetchall()
                has_time = any('time' in col[0].lower() for col in columns)
                has_sensor_id = any('sensor' in col[0].lower() or 'id' in col[0].lower() for col in columns)
                has_value = any('value' in col[0].lower() or 'val' in col[0].lower() for col in columns)
                
                if has_time and has_sensor_id and has_value:
                    query = f"INSERT INTO {target_table} (time, sensor_id, value) VALUES (%s, %s, %s)"
                elif len(columns) >= 3:
                    col_names = [col[0] for col in columns[:3]]
                    query = f"INSERT INTO {target_table} ({', '.join(col_names)}) VALUES (%s, %s, %s)"
                else:
                    self.log(f"Таблица {target_table} имеет несовместимую структуру", 'error')
                    t_conn.close()
                    return
                
                # Вставка порциями
                batch_size = 1000
                total_inserted = 0
                
                for i in range(0, len(data), batch_size):
                    batch = data[i:i + batch_size]
                    cur.executemany(query, batch)
                    total_inserted += len(batch)
                    
                    if i % 10000 == 0 and i > 0:
                        self.log(f"  Вставлено {total_inserted:,} из {count:,}...", 'info')
                
                dur = time.time() - t0
                self.log(f"✅ Успешно вставлено {count:,} строк за {dur:.2f} сек ({count/dur:.0f} строк/сек)", 'success')
                
                t_conn.close()
                
            except Exception as e:
                self.log(f"❌ Ошибка генерации: {e}", 'error')
                
        threading.Thread(target=task, daemon=True).start()
    
    # ================= ИНФО О ГИПЕРТАБЛИЦАХ =================
    
    def show_hypertables_info(self, parent_dialog=None):
        if parent_dialog:
            parent_dialog.destroy()
            
        try:
            cur = self.conn.cursor()
            query = """
                SELECT 
                    hypertable_name, 
                    num_chunks, 
                    pg_size_pretty(pg_total_relation_size(format('%I.%I', hypertable_schema, hypertable_name)::regclass)) as total_size
                FROM timescaledb_information.hypertables
                ORDER BY hypertable_name;
            """
            cur.execute(query)
            rows = cur.fetchall()
            
            win = tk.Toplevel(self.root)
            win.title("Информация о гипертаблицах")
            win.geometry("600x400")
            win.configure(bg=COLORS['bg_dark'])
            
            # Центрирование
            win.update_idletasks()
            width = win.winfo_width()
            height = win.winfo_height()
            x = (win.winfo_screenwidth() // 2) - (width // 2)
            y = (win.winfo_screenheight() // 2) - (height // 2)
            win.geometry(f'{width}x{height}+{x}+{y}')
            
            tk.Label(win, text="Гипертаблицы в базе данных", 
                    bg=COLORS['bg_dark'], fg=COLORS['orange_primary'],
                    font=('Segoe UI', 12, 'bold')).pack(pady=10)
            
            # Создаем Treeview
            tree_frame = tk.Frame(win, bg=COLORS['bg_dark'])
            tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            tree = ttk.Treeview(tree_frame, columns=("Таблица", "Чанки", "Размер"), show="headings", height=15)
            
            # Настройка стиля Treeview
            style = ttk.Style()
            style.configure("Treeview", 
                          background=COLORS['listbox_bg'],
                          foreground=COLORS['listbox_fg'],
                          fieldbackground=COLORS['listbox_bg'],
                          rowheight=25)
            style.configure("Treeview.Heading", 
                          background=COLORS['gray_dark'],
                          foreground=COLORS['text_primary'],
                          relief='flat')
            
            tree.heading("Таблица", text="Имя таблицы")
            tree.heading("Чанки", text="Кол-во чанков")
            tree.heading("Размер", text="Общий размер")
            
            tree.column("Таблица", width=250)
            tree.column("Чанки", width=100, anchor='center')
            tree.column("Размер", width=150, anchor='center')
            
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            
            tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            if not rows:
                tree.insert("", tk.END, values=("Нет гипертаблиц", "-", "-"))
            else:
                for r in rows:
                    tree.insert("", tk.END, values=r)
                    
        except Exception as e:
            self.log(f"Ошибка получения информации: {e}", 'error')
    
    # ================= СОЗДАНИЕ ТАБЛИЦЫ =================
    
    def create_table(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Создание новой таблицы")
        dialog.geometry("500x500")
        dialog.configure(bg=COLORS['bg_dark'])
        
        # Центрирование
        dialog.update_idletasks()
        width = dialog.winfo_width()
        height = dialog.winfo_height()
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f'{width}x{height}+{x}+{y}')
        
        main_frame = tk.Frame(dialog, bg=COLORS['bg_dark'], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(main_frame, text="Создание новой таблицы", 
                bg=COLORS['bg_dark'], fg=COLORS['orange_primary'],
                font=('Segoe UI', 14, 'bold')).pack(anchor='w', pady=(0, 20))
        
        # Имя таблицы
        tk.Label(main_frame, text="Имя таблицы:", 
                bg=COLORS['bg_dark'], fg=COLORS['text_primary']).pack(anchor='w')
        
        name_entry = tk.Entry(main_frame, 
                             bg=COLORS['input_bg'], fg=COLORS['text_primary'],
                             insertbackground=COLORS['orange_primary'])
        name_entry.pack(fill=tk.X, pady=(5, 15))
        
        # Поля таблицы
        fields_frame = tk.LabelFrame(main_frame, text="Поля таблицы", 
                                    bg=COLORS['bg_dark'], fg=COLORS['text_primary'])
        fields_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.new_fields = []
        
        def add_field(def_name="", def_type="FLOAT"):
            f_row = tk.Frame(fields_frame, bg=COLORS['bg_dark'])
            f_row.pack(fill=tk.X, pady=2, padx=5)
            
            e_name = tk.Entry(f_row, width=15, 
                             bg=COLORS['input_bg'], fg=COLORS['text_primary'],
                             insertbackground=COLORS['orange_primary'])
            e_name.pack(side=tk.LEFT, padx=2)
            e_name.insert(0, def_name)
            
            c_type = ttk.Combobox(f_row, values=["TIMESTAMPTZ", "FLOAT", "INTEGER", "TEXT", "BOOLEAN", "DATE"], 
                                 width=12, state="readonly")
            c_type.pack(side=tk.LEFT, padx=2)
            c_type.set(def_type)
            
            tk.Button(f_row, text="✖", command=lambda: remove_field(f_row),
                     bg=COLORS['error'], fg='white', width=3).pack(side=tk.RIGHT)
            
            self.new_fields.append((e_name, c_type))
        
        def remove_field(frame):
            for field in self.new_fields[:]:
                if field[0].master == frame:
                    self.new_fields.remove(field)
                    break
            frame.destroy()
        
        # Поля по умолчанию
        add_field("time", "TIMESTAMPTZ")
        add_field("sensor_id", "INTEGER")
        add_field("value", "FLOAT")
        
        # Кнопка добавления поля
        tk.Button(fields_frame, text="+ Добавить поле", 
                 command=lambda: add_field("new_column", "FLOAT"),
                 bg=COLORS['gray_medium'], fg=COLORS['text_primary']).pack(pady=10)
        
        def do_create():
            tbl = name_entry.get().strip()
            if not tbl:
                messagebox.showerror("Ошибка", "Введите имя таблицы!")
                return
                
            cols = []
            for e, c in self.new_fields:
                col_name = e.get().strip()
                col_type = c.get()
                if col_name:
                    cols.append(f"{col_name} {col_type}")
            
            if not cols:
                messagebox.showerror("Ошибка", "Добавьте хотя бы одно поле!")
                return
            
            sql = f"CREATE TABLE {tbl} ({', '.join(cols)});"
            
            try:
                cur = self.conn.cursor()
                cur.execute(sql)
                self.log(f"Таблица '{tbl}' создана", 'success')
                self.load_tables()
                dialog.destroy()
                messagebox.showinfo("Успех", f"Таблица '{tbl}' успешно создана!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось создать таблицу:\n{e}")
        
        # Кнопки
        btn_frame = tk.Frame(main_frame, bg=COLORS['bg_dark'])
        btn_frame.pack(fill=tk.X, pady=(20, 0))
        
        tk.Button(btn_frame, text="Создать таблицу", command=do_create,
                 bg=COLORS['orange_primary'], fg='white',
                 activebackground=COLORS['orange_dark'],
                 font=('Segoe UI', 10, 'bold'),
                 padx=20, pady=10).pack(side=tk.LEFT)
        
        tk.Button(btn_frame, text="Отмена", command=dialog.destroy,
                 bg=COLORS['gray_medium'], fg=COLORS['text_primary'],
                 padx=20, pady=10).pack(side=tk.RIGHT)
    
    # ================= НАСТРОЙКА БАЗЫ ДАННЫХ =================
    
    def setup_database(self):
        def task():
            try:
                cur = self.conn.cursor()
                self.log("Настройка базы данных...", 'info')
                
                # Включение TimescaleDB
                cur.execute("CREATE EXTENSION IF NOT EXISTS timescaledb;")
                self.log("Расширение TimescaleDB включено", 'success')
                
                # Создание стандартных таблиц
                cur.execute("DROP TABLE IF EXISTS sensors_plain CASCADE")
                cur.execute("""
                    CREATE TABLE sensors_plain (
                        time TIMESTAMPTZ NOT NULL,
                        sensor_id INTEGER NOT NULL,
                        value FLOAT NOT NULL
                    );
                """)
                
                cur.execute("DROP TABLE IF EXISTS sensors_hyper CASCADE")
                cur.execute("""
                    CREATE TABLE sensors_hyper (
                        time TIMESTAMPTZ NOT NULL,
                        sensor_id INTEGER NOT NULL,
                        value FLOAT NOT NULL
                    );
                """)
                
                # Создание гипертаблицы
                cur.execute("""
                    SELECT create_hypertable('sensors_hyper', 'time', 
                        chunk_time_interval => interval '7 days',
                        if_not_exists => TRUE);
                """)
                
                self.log("✅ База данных настроена:", 'success')
                self.log("   • sensors_plain - обычная таблица", 'success')
                self.log("   • sensors_hyper - гипертаблица", 'success')
                
                self.root.after(0, self.load_tables)
                
            except Exception as e:
                self.log(f"❌ Ошибка настройки: {e}", 'error')
                
        threading.Thread(target=task, daemon=True).start()
    
    # ================= ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ =================
    
    def run_performance_test(self):
        t1 = self.analyze_t1_var.get()
        t2 = self.analyze_t2_var.get()
        
        if not t1 or not t2:
            messagebox.showwarning("Ошибка", "Выберите обе таблицы для сравнения!")
            return

        self.log(f"\n--- ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ: {t1} vs {t2} ---", 'info')
        
        def task():
            try:
                cur = self.conn.cursor()
                
                # Проверяем структуру таблиц
                for table in [t1, t2]:
                    cur.execute(f"""
                        SELECT EXISTS (
                            SELECT 1 FROM information_schema.columns 
                            WHERE table_name = '{table}' 
                            AND column_name IN ('value', 'time')
                        )
                    """)
                    if not cur.fetchone()[0]:
                        self.log(f"❌ Таблица '{table}' не имеет нужных колонок (time, value)", 'error')
                        return
                
                results = []
                
                # Тест для каждой таблицы
                for i, table in enumerate([t1, t2], 1):
                    query = f"""
                        SELECT AVG(value) 
                        FROM {table} 
                        WHERE time > NOW() - INTERVAL '7 days'
                    """
                    
                    # Выполняем 5 раз для усреднения
                    times = []
                    for _ in range(5):
                        t0 = time.perf_counter()
                        cur.execute(query)
                        cur.fetchall()
                        times.append((time.perf_counter() - t0) * 1000)  # в мс
                    
                    avg_time = sum(times) / len(times)
                    results.append((table, avg_time))
                    
                    self.log(f"{i}️⃣ {table}: {avg_time:.2f} мс (минимум: {min(times):.2f} мс)", 'info')
                
                # Сравнение результатов
                table1, time1 = results[0]
                table2, time2 = results[1]
                
                if time1 > time2:
                    ratio = time1 / time2
                    winner = table2
                    faster = f"{ratio:.1f}x"
                else:
                    ratio = time2 / time1
                    winner = table1
                    faster = f"{ratio:.1f}x"
                
                self.log(f"🏆 {winner} быстрее в {faster}", 'success')
                
            except Exception as e:
                self.log(f"❌ Ошибка теста: {e}", 'error')
                
        threading.Thread(target=task, daemon=True).start()
    
    def run_explain(self):
        target_table = self.analyze_t2_var.get()
        if not target_table:
            messagebox.showwarning("Ошибка", "Выберите таблицу для анализа!")
            return
            
        query = f"EXPLAIN ANALYZE SELECT AVG(value) FROM {target_table} WHERE time > NOW() - INTERVAL '1 hour'"
        
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            result = "\n".join([r[0] for r in rows])
            
            win = tk.Toplevel(self.root)
            win.title(f"EXPLAIN ANALYZE: {target_table}")
            win.geometry("800x500")
            win.configure(bg=COLORS['bg_dark'])
            
            text_frame = tk.Frame(win, bg=COLORS['bg_dark'])
            text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            tk.Label(text_frame, text=f"Запрос: {query}", 
                    bg=COLORS['bg_dark'], fg=COLORS['text_orange'],
                    font=('Consolas', 9)).pack(anchor='w', pady=(0, 10))
            
            text = scrolledtext.ScrolledText(text_frame, 
                                           width=100, 
                                           height=30, 
                                           font=('Consolas', 9),
                                           bg=COLORS['log_bg'],
                                           fg=COLORS['log_fg'])
            text.pack(fill=tk.BOTH, expand=True)
            text.insert(tk.END, result)
            text.config(state='disabled')
            
        except Exception as e:
            self.log(f"Ошибка explain: {e}", 'error')
    
    # ================= ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ =================
    
    def log(self, msg, msg_type='info'):
        ts = datetime.now().strftime('%H:%M:%S')
        
        if msg_type == 'error':
            color = COLORS['log_error']
            prefix = "❌ "
        elif msg_type == 'success':
            color = COLORS['log_success']
            prefix = "✅ "
        elif msg_type == 'warning':
            color = '#FFA726'  # оранжевый
            prefix = "⚠️  "
        else:
            color = COLORS['log_fg']
            prefix = "ℹ️  "
        
        self.log_area.insert(tk.END, f"[{ts}] {prefix}{msg}\n")
        
        # Применяем цвет к последней строке
        start_index = self.log_area.index(f"end-{len(msg)+20}c")
        end_index = self.log_area.index("end-1c")
        self.log_area.tag_add(msg_type, start_index, end_index)
        self.log_area.tag_config(msg_type, foreground=color)
        
        self.log_area.see(tk.END)
    
    def create_btn(self, parent, text, command, color='gray'):
        if color == 'orange':
            bg = COLORS['btn_orange']
            hover = COLORS['btn_orange_hover']
            fg = 'white'
        elif color == 'error':
            bg = COLORS['error']
            hover = '#D32F2F'
            fg = 'white'
        else:
            bg = COLORS['btn_gray']
            hover = COLORS['btn_gray_hover']
            fg = COLORS['text_primary']
        
        return tk.Button(parent, text=text, command=command,
                        bg=bg, fg=fg,
                        activebackground=hover,
                        activeforeground=fg,
                        font=('Segoe UI', 10),
                        relief='flat',
                        padx=15, pady=8,
                        cursor='hand2')

if __name__ == "__main__":
    root = tk.Tk()
    app = TimescaleLabApp(root)
    root.mainloop()