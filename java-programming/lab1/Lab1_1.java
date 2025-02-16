import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ToggleButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Lab1_1 extends Application {

    private List<ImageView> images = new ArrayList<>();
    private ToggleGroup toggleGroup = new ToggleGroup();

    @Override
    public void start(Stage primaryStage) {
        Pane pane = new Pane();
        pane.setOnMouseClicked(event -> {
            if (event.getButton().toString().equals("SECONDARY")) {
                ToggleButton selectedButton = (ToggleButton) toggleGroup.getSelectedToggle();
                if (selectedButton != null) {
                    ImageView imageView = new ImageView(((ImageView) selectedButton.getGraphic()).getImage());
                    imageView.setX(event.getX());
                    imageView.setY(event.getY());
                    pane.getChildren().add(imageView);
                    images.add(imageView);
                }
            }
        });

        VBox vbox = new VBox(10);
        for (int i = 1; i <= 5; i++) {
            ToggleButton button = new ToggleButton();
            button.setGraphic(new ImageView(new Image("image" + i + ".png")));
            button.setToggleGroup(toggleGroup);
            vbox.getChildren().add(button);
        }

        Button saveButton = new Button("Сохранить");
        saveButton.setOnAction(event -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Сохранить изображение");
            File file = fileChooser.showSaveDialog(primaryStage);
            if (file != null) {
                try (FileOutputStream out = new FileOutputStream(file)) {
                    // Сохранение изображения
                    // Здесь нужно реализовать сохранение изображения
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });

        HBox root = new HBox(10, pane, vbox, saveButton);
        Scene scene = new Scene(root, 800, 600);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}