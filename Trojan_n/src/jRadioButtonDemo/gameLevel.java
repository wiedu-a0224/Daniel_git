package jRadioButtonDemo;

import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.border.Border;

public class gameLevel {
	
	JPanel panSpeed = new JPanel();
	add(panSpeed);
	panSpeed.setBounds(20, 20, 80, 120);
	Border lineB = BorderFactory.createLineBorder(Color.black);
	panSpeed.setBorder(BorderFactory.createTitledBorder(lineB, "����"));
	panSpeed.setLayout(new FlowLayout(FlowLayout.LEFT));
	ButtonGroup group = new ButtonGroup();
	JRadioButton[] rdb = new JRadioButton[2];
	rdb[0] = new JRadioButton("�з�", true);
	rdb[1] = new JRadioButton("��");
	rdb[0] = new JRadioButton("�ܧ�", true);
	rdb[1] = new JRadioButton("����");
	for (int i = 0; i < rdb.length; i++) {
		group.add(rdb[i]);
		panSpeed.add(rdb[i]);
	}	
	
	rdb[0].addActionListener(new ActionListener() {
		public void actionPerformed(ActionEvent arg0) {
			 A=1500;
			;
		}
	});
	
	rdb[1].addActionListener(new ActionListener() {
		public void actionPerformed(ActionEvent e) {
			 A = 1000;
		}
	});
	
	rdb[2].addActionListener(new ActionListener() {
		public void actionPerformed(ActionEvent arg0) {
			 A = 750;
			;
		}
	});
	
	rdb[3].addActionListener(new ActionListener() {
		public void actionPerformed(ActionEvent e) {
			 A = 50;
		}
	});
	
}
