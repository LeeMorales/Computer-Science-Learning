#include <QApplication>
#include <Qdialog>
#include <QLabel>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);QDialog w;
  w.resize(500, 600);
  QLabel label(&w);
  label.move(200, 200);
  label.setTet("Henllo");
  w.show();

  return a.exec();

}