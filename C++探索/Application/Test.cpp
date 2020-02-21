#include <QApplication>
#include <Qdialog>
#include <QLabel>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);QDialog w;
  w.resize(500, 600);
  QLabel label(&w);
  
}