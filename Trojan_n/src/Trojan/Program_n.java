package Trojan;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.*;


class AJFrame extends JFrame  {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	// 12(0~11)��첾�ι�,4(12~549)��D���
	private JLabel[] jlbl = new JLabel[50];
	// �ڭx0.png, 1.png, �ĭx2.png, �ť�3.png,4(4~17)�D��I����
	private ImageIcon[] icons = new ImageIcon[18];
	// jlblSum "�ڭx��^�ƶq",jlblLoss "�ڭx�Y�e+�ĭx�L�e�ƶq"
	private JLabel jlblSave, jlblLoss, jlblForce;
	// jbtnStart "�}�l�C��",jbtnPull"�ɾ�" ���s
	private JButton jbtnStart, jbtnPull;
	
	

	private int save = 0, z = 0, k = 0, A = 1500;
	private int loss = 0, force = 100;
	private boolean b = true;

	// �غc��
	AJFrame() {
		// ���ϥΪ����t�m
		super.setLayout(null);
		// �������D
		super.setTitle("�차�O���O");
		// �]�wicons����ӷ�warImg��Ƨ�
		for (int i = 0; i < icons.length; i++) {
			icons[i] = new ImageIcon(".\\warImg\\" + String.valueOf(i) + ".png");
		}
		// �إ�jlbl[0]~jlbl[11]�A���w��Ljlbl[]���ťչ�(3.png)
		int g = 11;
		for (int i = 0; i < g; i++) {
			jlbl[i] = new JLabel();
			jlbl[i].setBounds(i * 75 + 60, 400, 75, 75);
			jlbl[i].setIcon(icons[3]);
			add(jlbl[i]);
		}
		jlbl[g] = new JLabel();
		jlbl[g + 1] = new JLabel();
		jlbl[g + 2] = new JLabel();
		jlbl[g + 3] = new JLabel();
		jlbl[g + 4] = new JLabel();
		jlbl[g + 5] = new JLabel();

		jlbl[g].setBounds(50, 475, 517, 75);// ���a���Ϧ�m�j�p
		jlbl[g].setIcon(icons[4]);// ���a����4.png
		jlbl[g + 1].setBounds(650, 475, 270, 75);// �u�a���Ϧ�m�j�p
		jlbl[g + 1].setIcon(icons[5]);// �u�a����5.png
		jlbl[g + 2].setBounds(745, 10, 200, 500);// �����Ϧ�m�j�p
		jlbl[g + 2].setIcon(icons[6]);// ������6.png
		jlbl[g + 3].setBounds(570, 475, 100, 75);// ����m�j�p
		jlbl[g + 3].setIcon(icons[8]);// ������7.png���U��8.png
		jlbl[g + 4].setBounds(570, 550, 100, 75);// �Y����m�j�p
		jlbl[g + 4].setIcon(icons[3]);// �Y����m��
		jlbl[g + 5].setBounds(50, 70, 200, 500);// �차��m�j�p
		jlbl[g + 5].setIcon(icons[9]);// �차��9.png
		add(jlbl[g]);
		add(jlbl[g + 1]);
		add(jlbl[g + 2]);
		add(jlbl[g + 3]);
		add(jlbl[g + 4]);
		add(jlbl[g + 5]);

		jlblSave = new JLabel("�ڭx�䴩�ƶq�G" + String.valueOf(save));
		jlblSave.setBounds(180, 50, 180, 20);
		jlblSave.setFont(new Font("�L�n������", Font.PLAIN, 18));
		add(jlblSave);

		jlblLoss = new JLabel("�ڭx�ԤO�l���q�G" + String.valueOf(loss));
		jlblLoss.setBounds(380, 50, 180, 20);
		jlblLoss.setFont(new Font("�L�n������", Font.PLAIN, 18));
		add(jlblLoss);

		jlblForce = new JLabel("�u����O�ȡG" + String.valueOf(force) + "%");
		jlblForce.setBounds(600, 50, 180, 20);
		jlblForce.setFont(new Font("�L�n������", Font.PLAIN, 18));
		add(jlblForce);

		// jbtnStart�C���}�l�s
		jbtnStart = new JButton("�}�l�C��");
		jbtnStart.setBounds(200, 580, 150, 60);
		jbtnStart.setFont(new Font("�L�n������", Font.PLAIN, 24));
		add(jbtnStart);

		// jbtnPush�ɾ��s
		jbtnPull = new JButton("�� �� ��");
		jbtnPull.setBounds(700, 580, 150, 60);
		jbtnPull.setFont(new Font("�L�n������", Font.PLAIN, 24));
		add(jbtnPull);

		jbtnStart.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent evt1) {
				Thread t = new Thread(new Runnable() {
					public void run() {
						// �üƭ�
						int[] n = new int[18];
						for (int i = 0; i < 11; i++) {
							if (i <= 11)
								n[i] = 3;
						}
						jbtnStart.setEnabled(false); // ���୫�ƫ��C���}�l���s

						try {
							do {

								// jlbl[0]~jlbl[11]��ܼĭx �ڭx �ťչϥ�
								for (int i = 18; i >= 0; i--) {
									// �j��9��n[]�D���ʪ��L�ϡA���L���B�z
									if (i > 9)
										continue;

									n[i + 1] = n[i];// ����array���ȡA���{�L�V�k����
								} // �C�j�@����Jn[0]=�ťչϡA�קK��ܤӹL����
								if (k % 2 == 0) {
									n[0] = 3;
								} else {
									// �H������n[0]=0 1 2 3
									n[0] = (int) Math.round(Math.random() * 3);
								}
								if (z % 2 == 0) {
									b = false;
								} else
									b = true;
								// �ĭx�L�e��F�����A�ԤO�l��+1
								if (n[7] == 2 && b)
									loss++;
								if (n[7] == 1 && b)
									loss++;
								// �ڭx�L�e
								if (n[7] == 0 && b)
									save++;
								
								// �ڭx�Y�e���n[7]�ťչ�n[15]�L��
								if (n[7] == 0 && !b) {
									n[7] = 3;
									loss++;
									jlbl[15].setIcon(icons[10]);

								}
								
								// �ĭx�Y�e���n[7]�ťչ�n[15]�L��
								if (n[7] == 1 && !b) {
									n[7] = 3;
									jlbl[15].setIcon(icons[11]);

								}
						
								if (n[7] == 2 && !b) {
									n[7] = 3;
									jlbl[15].setIcon(icons[12]);

								}
								while (true) {
									if (save >= 10 && loss > 0) {
										loss--;
										save -= 10;
									} else
										break;
								}
								for (int j = 0; j < 11; j++) {
									jlbl[j].setIcon(icons[n[j]]);
								}
								System.out.print("z=" + z + ", sum=" + save + ", loss=" + loss);
								System.out.println(", b=" + b + ", n[7]=" + n[7] + ", k=" + k);

								k++;
								Thread.currentThread();
								Thread.sleep(A);
//								wait(1500);

								jlblSave.setText("�ڭx�䴩�ƶq�G" + String.valueOf(save) + "\t�H");
								jlblLoss.setText("�ڭx�ԤO�l���q�G" + String.valueOf(loss) + "\t�H");
								jlblForce.setText("�u����O�ȡG" + String.valueOf((force - loss * 10) + "%"));
								
							} while (loss < 10); // �Yloss=10�A�h����C��
						} catch (InterruptedException ex) {
						} finally {
							jlbl[13].setIcon(icons[13]);// ������13.png
							JOptionPane.showMessageDialog(null, "�����w�g�Q��}!\n�Ы��}�l���s���C��");
							jbtnStart.setEnabled(true);
							loss = 0;
							save = 0;
							jlbl[13].setIcon(icons[6]);
							jlbl[15].setIcon(icons[3]);
						}

					}
				});
				t.start(); // �Ұʰ����
			}
		});

		jbtnPull.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent evt2) {
				Thread h = new Thread(new Runnable() {
					// �}�Ҿ���
					public void run() {
						jbtnPull.setEnabled(true);
						if (z % 2 == 0) {
							jlbl[14].setIcon(icons[7]);
						} else
							jlbl[14].setIcon(icons[8]);
						z++;// ���ѥ��L��b���p��
					}
				});
				h.start();
			}
		});

		JPanel panSpeed = new JPanel();
		add(panSpeed);
		panSpeed.setBounds(450, 180, 80, 150);
		Border lineB = BorderFactory.createLineBorder(Color.black);
		panSpeed.setBorder(BorderFactory.createTitledBorder(lineB, "����"));
		panSpeed.setLayout(new FlowLayout(FlowLayout.LEFT));
		ButtonGroup group = new ButtonGroup();
		JRadioButton[] rdb = new JRadioButton[4];
		rdb[0] = new JRadioButton("�з�", true);
		rdb[1] = new JRadioButton("��");
		rdb[2] = new JRadioButton("�ܧ�");
		rdb[3] = new JRadioButton("����");
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
				 A = 500;
			}
		});
		
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);// �]�w�������������s�|�����{��
		setSize(980, 750);
		setLocationRelativeTo(null);
		setVisible(true);

	}
}

//�D�{��
public class Program_n {
	public static void main(String[] args) {
		// �إ�AJFrame����(�차�O���O�C��)
		new AJFrame();
	}
}
