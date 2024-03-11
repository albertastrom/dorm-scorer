# **Colby 2023-2024 Doubles Ranking**

By Albert Astrom

## **System Overview**

The Colby room selection process works by assigning each student a one minute time slot for them to pick from the remaining pool of rooms. The assignment of times is randomly generated within each class year, however picking order is determined by seniority in that rising seniors pick on the first day, rising juniors the next, and rising sophomores last. 

In order to maximize the chances of being satisfied with housing next year, this process will rank each double on campus empirically with a consistent scale to present the best available choice. This will allow for an objective selection process that will make choosing a room during the assigned slot less stressful and more efficient. 

Each room is ranked based on the following seven weighted criteria:

```
1. Number of Rooms (weight: 0.38)
1. Square Footage (weight: 0.18)
1. Location (weight: 0.12)
1. Proximity to Bathroom (weight: 0.09)
1. Floor (weight: 0.1)
1. Number of Windows (weight: 0.09)
1. Likeability (0.04)
```

## **Algorithm**

The program uses a weighted scoring algorithm to assign a value to each room to compare them by. This comparison can then be used to sort the rooms for the best features while looking for the same things each time. Each criteria is normalized using min-max normalization to make sure weights are counted properly. 

## **Criteria Breakdown and Rating Guide**

The spreadsheet is structured using 8 columns (room ID + 7 criteria) and each row corresponds to a room. For each room you will fill in the corresponding values in the columns. The order you do this in will not matter, but it would be easiest to go by building and then floor. 

Here is how to fill in each column… 

### **Room ID**

The room ID is simply the building identifier + room number.

The building identifiers are as follows:
```
(Building - Code)
- AMS - A
- Coburn - C
- Dana - D
- Drummond - DR
- East - E
- Foss - F
- Goddard-Hodgkins - G
- Heights - H
- Johnson Pond 3 - JPT
- Johnson Pond 4 - JPF
- Mary-Low - M
- Perkins-Wilson - PW
- Pierce - P
- Roberts - R
- Treworgy - T
- Woodman - W
```

So, Pierce 211 would have room ID `P211`.

### **Number of Rooms**

The ideal living situation involves privacy and personal space. For this reason, an ideal double will have two rooms to maximize privacy and better define personal space. Though two room doubles usually come at the cost of some square footage, it is arguably a worthy sacrifice. 

In the spreadsheet, simply write the number of bedrooms (likely either 1 or 2).


### **Square Footage**

More space is more livable and is better in nearly every way. 

In the spreadsheet, write the square footage as a number without units.

### **Location**

While it’s hard to say exactly where one will want to spend most of their time next year, generally speaking some areas are likely to be more convenient than others. Proximity to a dining hall, the athletic center, and class buildings are considered.

In the spreadsheet, write the location number as defined in the following image:
<https://drive.google.com/file/d/1uVHhFxTna3qK7wI_k6ZG06PzAwNoDkZA/view?usp=share_link>

### **Proximity to Bathrooms**

While this one is livable regardless, it can be a huge inconvenience if you have to go to a different floor to find a bathroom. 

In the spreadsheet, write the number that corresponds to the following scale:


```
1 - next door / a few doors down

2 - down the hall

3 - different floor next to stairwell

4 - different floor down the hall
```


### **Floor**

While living on the ground floor can be nice for going in and out of the dorm building, it can feel invasive to have people walking by your window frequently. This could encourage keeping blinds down.

In the spreadsheet, write the number that corresponds to the following scale:

```
1 - ground floor

2 - 2nd or 3rd floor 
```

### **Number of Windows**

More windows means more light. It’s not a huge consideration, but more sunlight can improve mood, which is essential for the winter months. More windows can also allow for more ventilation.

In the spreadsheet, enter the number of windows the room has.

### **Likeability**

There's a chance that a room will check all of the boxes and still feel wrong. This rating can also encompass any factor that wasn’t considered in the other six. Generally, a room will get a standard rating, but this criteria still gives the opportunity to influence the rating in case the room is not at that level.

In the spreadsheet, write the number that corresponds to the following scale:

```
1 - standard 

2 - slightly off

3 - very off
```

### **Example**

Dana 127 would have the following numbers:

(Room ID, Number of rooms, Square footage, Location, Proximity to Bathroom, Floor, Number of windows, Likeability)

`D127, 1, 186, 3, 1, 1, 1, 1`

## **Links**

Spreadsheet: 

[Doubles Room Rank](https://docs.google.com/spreadsheets/d/1iNgbPg7el4IeEMWJMwpXAPaEGJqYV0vTpe3bg1LhcbA/edit?usp=sharing)

Floor plans (now defunct):

<https://life.colby.edu/wp-content/uploads/2023/04/2023-Room-Draw-Upperclass.pdf>


