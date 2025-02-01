from django.shortcuts import render
data=[{'id':1,'title':'Python',
       'Info':[{'point':'Proficient in Python programming with experience in writing efficient and maintainable code.'},
 {'point':'Skilled in variables, data types, and control structures such as loops and conditionals for implementing logic-driven solutions.'},
 {'point':'Knowledgeable in Python data structures, including lists, dictionaries, tuples, and sets for effectivedata management.'},
 {'point':'Expertise in working with functions and modular programming to create reusable and organizedcode.'},
 {'point':'Proficient in file handling operations, including reading, writing, and manipulating text, JSON, CSV, and binary files, with robust implementation of exception handling for reliable data processing.'},
 {'point':'Experienced in working with iterators and generators to create efficient and memory-friendly code for iterative tasks.'},
  {'point':'Skilled in implementing shallow and deep copy techniques to manage object references and ensure data integrity during object cloning.'},
   {'point':'Skilled in applying searching algorithms, sorting techniques, and data structure operations, including stacks and queues.'}]},
      {'id':2,'title':'SQL',
       'Info':[{'point':'Extensive experience in writing SQL queries and performing CRUD operations on RDBMS (Relational Database Management Systems).'},
 {'point':'Proficient in Joins, Subqueries, and solving queries.'},
 {'point':'Strong understanding of SQL concepts like Pseudo Columns, Grouping, and built-in SQL functions.'},
 {'point':'Skilled in using DDL (Data Definition Language), DML (Data Manipulation Language), TCL (Transaction Control Language), and DCL (Data Control Language).'},
 {'point':'Hands on experience with database systems including Oracle, SQL Server, and MySQL.'},
 {'point':'Proficient in database normalization up to 5NF (First, Second, Third Normal Form, Boyce-Codd Normal Form, and Fifth Normal Form).'}]},
      {'id':3,'title':'C and Java','Info':[{'point':'Basics'}]},
      {'id':4,'title':'HTML',
       'Info':[{'point':'Proficient in using semantic and non-semantic HTML tags for structured and meaningful content.'},
 {'point':'Skilled in applying local and global attributes for enhanced HTML functionality.'},
 {'point':'Experienced in inserting media files and hyperlinks for dynamic web pages.'},
 {'point':'Able to create lists and tables to organize content effectively.'}]},
      {'id':5,'title':'CSS',
       'Info':[{'point':'Knowledgeable in using different types of CSS, including selectors, combinators, and pseudoselecors.'},
 {'point':'Proficient in applying CSS properties such as the box model (margin and padding), position, and display.'},
 {'point':'Understands principles of responsive design for optimized user experience across devices.'},
 {'point':'Basic experience in creating animations using CSS.'}]},
      {'id':6,'title':'JavaScript',
       'Info':[{'point':'Strong understanding of JavaScript keywords, variables (including scope), and data types.'},
 {'point':'Familiar with ES6 features like arrow functions, template literals, destructuring, and modules.'},
 {'point':'Skilled in using operators, including arithmetic, comparison, spread, and rest operators.'},
 {'point':'Proficient in working with functions, arrays, objects, and strings, with knowledge of destructuring and hoisting.'},
 {'point':'Experience with the Browser Object Model (BOM) to handle events, location, popups, and timing functions.'},
 {'point':'Experienced in manipulating the DOM, performing data validation, and using promises, async, and await for asynchronous operations.'}]},
      {'id':7,'title':'Python','Info':[{'point':'Basics'}]}
 ]
# Create your views here.
def skill(request):
    context={'record':data}
    return render(request,'skill.html',context)

def read(request,id):
    for i in data:
        if i['id']==id:
            context={'record':i}
    return render(request,'read.html',context)