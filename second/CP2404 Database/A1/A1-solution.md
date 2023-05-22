1. Identify entities through narrative description

- Catch nouns in the description.
- Determine whether you want to collect any information about that object.

  - If "yes", keep it as a potential entity.
  - If "No", leave it out.

- Nouns

  - schools, children, training sessions, competitions, shcool holidays, branch, enrollment, places, staff, equipment, customers,
    billing rate
  - branch
    - ID number
    - district
    - name,
    - location
    - details of employees
    - branch manager
  - employee
    - salary
    - branch
    - details
    - previous manager
    - other employees
    - professional training staff, admin staff,
    - permanently employed
      - personnel information
      - qulification
      - certification start/end
      - access card
        - ID, faulty, he building sections it allows access to, employee name,
      - ipad
        - ID, faulty, model, color, other specifications, history of repair, employee name, purchase date, date assigned,
    - local staff
      basic information(name, contact, address, DOB. start date, end date, payment rate, work hours)
      access card
  - customer
    contact details, mail address, name, child,

  - billing rates

    - 15% for staff
    - 10 for valued customers
    - start from date,
    - end date,

  - Children
    - name, date of birth, gender, height, weight, digital photo
    - comment
    - start date
    - coaching date, If the child did not attend coaching at the school for 6 months, then a reminder notice is mailed to the parent.
  - training session
    training done, the trainer details, number of hours, unit price
    session id, session name,
  - sports gear
    price

  - invoice
    invoice number
    invoice date
    child name,
    session name
    session hour
    discount

  ## entities

        - branch
        - employee
        - customer
        - children
        - equipment
        - access_card
        - training_session
        - sport_gear
        - invoice

2. Identify Relationships among entities

   branch - employee 1 : M
   branch - customer M : N
   customer - children 1 : M
   employee - equipment 1 : M
   employee - access_care 1 : M
   children - training-session M : N
   children - sport_gear M : N
   customer - invoice 1 : M

3. Identify attributes

   - branch

     - branch_id
     - district
     - location
     - manager

   - employee

     - employee_id
     - name,
     - contact,
     - address,
     - DOB,
     - branch_id
     - previous manager
     - training staff or admin staff
     - qualification
     - certification start date
     - certificaiton end date
     - salary

   - casual worker

     - id
     - name,
     - contact,
     - address,
     - DOB,
     - start_date
     - end date
     - payment rate,
     - work hours

   - customer

     - contact
     - name
     - children
     - name

   - children

     - children_id
     - name
     - date of birth
     - gender
     - height
     - weight
     - digital photo
     - training_session_id
     - training\*session_start_date
       - training_session_end_date

   - training session

     - trainng session id
     - training session name
     - trainer_id(FK)
     - unit_price
     - number of hours

   - sport gear

     - sport gear id
     - sport gear name
     - sport gear detail information
     - unit price
     - quantity

   - invoice
     invoice number
     invoice date
     child name,
     session name
     session hour
     discount

   - equipment
     - ID, faulty, model, color, other specifications, history of repair, employee name, purchase date, date assigned,

   A branch must have one to many employees.
   An employee belongs to one and only one branch.
   A branch has one and only one employee as manager.
   An employee may not manage a branch(zero to one).
   A branch may hire local casual workers (zero to many).
   A casual worker works at one branch (one and only one).
   A casual work has different working hours each month.
   A work hour record belongs to one casual worker.
   A building can be accessed by many access_cards.
   An access_card cab access to many buildings(one to many).
   An access card belongs to one and only one casual worker.
   A casual worker has zero to one access_card.
   An access card belongs to one and only one employee.
   An employee has zero to one access_card.
   An employee has one and only one staff type(trainer or admin).
   A staff type can be used by many employees.
   An employee may have one previous manager.
   An employee can be previous manager of many employees.
   An employee may have one current manager.
   An employee can be current manager of many employees.
   An employee may have an ipad.
   An ipad can be assigned to an employee.
   An employee may have different salaries.
   A salary belongs to one employee.
   A customer may have many children.
   A child has one and only one parent.
   A child may have sport gear.
   A type of gear can be sold to zero to many children.
   An employee can be trainer of different training session.
   A training session can taught by different employees(trainers).
   A child may attend different training sesssion.
   A training session can have zero to many children.
