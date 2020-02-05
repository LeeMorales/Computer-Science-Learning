// Hengyi Li
// The purpose of the program is to store student record information by using a collection class
//This code done by Hengyi Li at 8:30 PM 28th Jan, 2020
//Copyright Hengyi Li

#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

// file name
const string FILE_NAME = "student_record.txt";

// menu choices
enum MenuOptions{ADD_NEW, VIEW_ALL, SEARCH, DELETE, SAVE_ALL, EXIT};

// student class
class Student
{
  private:
    unsigned id;  // positive value
    string name;  // name with space allowed
  public:
    void setName(string n)
    { 
      name = n;
    }
    
    string getName()
    { 
      return name;
    }
    
    void setID(int id_param)
    { 
      id = id_param;
    }
    
    int getID()
    { 
      return id;
    }
    
    // creating a single string value out of
    // all the fields of the student object
    string string_format()
    { 
      string result = to_string(id) +" -- " + name;
      return result;
    }

}; // student class ends.


// this collection class employs a vector variable to store
// student records
class StudentCollection
{
  private:
     vector<Student> student_records; // holds all student records 
  
  public: 
    
  void load_all_records()
  { // TODO as soon as the program starts,
    // read the student record entries from the file FILE_NAME and
    // create student objects for each entry
    Student newStudent_id;
    Student newStudent_name;

    ifstream data_file;
    data_file.open(FILE_NAME);

    string Name_of_student;
    data_file >> Name_of_student;

    int id_of_student;
    data_file >> id_of_student;
    // add them to the student_records collection
    newStudent_name.setName(Name_of_student);
    newStudent_id.setID(id_of_student);
  }
  
  
  // this function will input values for a new movie record
  // and will return that
  void add_new_record()
  {
    // TODO input the values for the student record (id and name)
    unsigned id;
    string name;
    cout << "Student ID: ";
    cin >> id;
    string dummy;
    getline(cin,dummy);
    cout << "Student Name: ";
    getline(cin, name);
   
    
    // TODO use the public methods to initialize the student object
    Student newStudent;

    // add the object in the student records vector
    newStudent.setName(name);
    newStudent.setID(id); 
    student_records.push_back(newStudent);   
  }
  
  
  
  
  // search the student records based on title
  int find_student_record(unsigned search_id)
  { 
    for(size_t index = 0; index<student_records.size();index++)
    {
      if(student_records[index].getID() == search_id)
      {
        cout << endl << "The record has been found: ";
        cout<< student_records[index].string_format();
        return index;
      }
      else
      {
        cout << endl << "The record was not found: ";
      }
    }
  return - 1; // a negative value to indicate the record has not been found
  }


  // if there is a student with delete_id in the record then that record would be deleted
  // otherwise, nothing happens.
  void delete_record(int delete_id)
  { 
    // call the find_student_record(delete_id) and store the returned value
    int position = find_student_record(delete_id);
    
    // TODO if the return value is a positive value then
    if(position > 0)
    {
      student_records.erase(student_records.begin() + position);
    }
    // TODO if successful then display 
   cout << endl << "the record had been deleted";
  }

  // view all student records
  void view_all_records()
  {
    cout << endl << endl << "We have the following student records: ";
    // use a loop and call the to_string method to display the records
    for(unsigned i=0;i<student_records.size();i++)
    {  // display the student records
    }
  }
  
  // save all the record in the vector to a file
  void save_all_records()
  { // TODO when this option is selected, open the FILE_NAME in write mode
    ofstream output_file;
    output_file.open(FILE_NAME);
    // write each student object information in one single line in the file
    Student all_records;
    string dummy;
    for(unsigned looptimes = 0; looptimes < student_records.size();looptimes++)
    {
      output_file << all_records.string_format(); 
      getline(cin,dummy);
    }
    // write a confirmation that the operation was successful
    cout << "Successfully saved";
    output_file.close();
  }

}; // studentcollection class ends




// display the menu and return the selection
int display_menu()
{
  cout << endl << endl << to_string(ADD_NEW) +  ". Add a new student record" << endl
      << to_string(VIEW_ALL) + ". View all student records" << endl
      << to_string(SEARCH) + ". Find a record by its ID number" << endl
      << to_string(DELETE) + ". Delete a student record" << endl
      << to_string(SAVE_ALL) + ". Save all student records in file" << endl
      << to_string(EXIT) + ". Exit the program" << endl
      << "Your choice: ";

  int choice = EXIT; // default choice is exit

  cin >> choice; // getting the user's choice

  return choice;
}





// the main function
int main()
{
  int choice = EXIT;  // gets the choice from the user
  StudentCollection myStudentRecords;

  // load all student entries from the file, create objects, and add them in the collection
  myStudentRecords.load_all_records();
  
  do {
    choice = display_menu();

    switch(choice)
    {
      case ADD_NEW: // add new record
  
        myStudentRecords.add_new_record();
        break;

    
      case SEARCH: // search based on title
        int search_id;

        // get the ID to search from the user
        cout<<endl<<"Enter the ID that you want to search: ";
        cin>>search_id;
        cin.ignore(); // consume the new line character

        myStudentRecords.find_student_record(search_id);
        break;
   
      case VIEW_ALL: // view all records
    
        // call the function view_all_records to display all student records
        myStudentRecords.view_all_records();
        break;
    
    
      case DELETE: // delete a record
        int delete_id;
        cout<<endl<<"Enter the ID that you want to delete: ";
        cin>>delete_id;
        cin.ignore(); // consume the new line character
        myStudentRecords.delete_record(delete_id);
        break;
      
      
      case SAVE_ALL: // save all student object entries in a file
        myStudentRecords.save_all_records();
        cout<<endl<<"Success! all records have been saved.";
        break;
        
      case EXIT: // Exit the program
        cout<<endl<<"Thanks for using the program";
        break;
      
      default:
        cout << endl << "Invalid choice. Try again: ";
        break;
    }

  } while (choice != EXIT); // exit condition
  return 0;
}