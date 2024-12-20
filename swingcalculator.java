
import javax.swing.*;
import java.awt.event.*;

public class Swing {
    public static void main(String[] args) {
        // Create a JFrame
        JFrame frame = new JFrame("Swing Example");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        // Create a JLabel
        JLabel label = new JLabel("Enter your name:");
        label.setBounds(50, 30, 150, 25);
        frame.add(label);

        // Create a JTextField
        JTextField textField = new JTextField();
        textField.setBounds(200, 30, 150, 25);
        frame.add(textField);

        // Create a JButton
        JButton button = new JButton("Greet Me");
        button.setBounds(150, 80, 100, 30);
        frame.add(button);

        // Create an ActionListener for the button
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String name = textField.getText();
                JOptionPane.showMessageDialog(null, "Hello, " + name + "!");
            }
        });

        frame.setVisible(true);
    }
}
