

         MODEL DEFAULTS
         --------------

Model Name:         BLAZE
Model Description:  
Output File:        BLAZE.out
Output Plot Style:  NOAUTO_FIT
Run Mode:           HI_SPEED
Trace Vars:         SERVICE[ID[7]],SYSTEM[ID[7]],RATIO[0],RATIO[3],WAIT[ID[7]]
Random Number Seed: 970
Initial Values:     
Ending Condition:   STOP_ON_TIME
Ending Time:        1000.000
Trace Events:       DELIVER
Hide Edges:         



         STATE VARIABLES
         ---------------

     State Variable #1
Name:          SYSTEM
Description:   Time in system
Type:          REAL
Size:          1000

     State Variable #2
Name:          SERVICE
Description:   Time being served (first)
Type:          REAL
Size:          1000

     State Variable #3
Name:          QUEUE
Description:   
Type:          INTEGER
Size:          2

     State Variable #4
Name:          SERVER
Description:   
Type:          INTEGER
Size:          2

     State Variable #5
Name:          ID
Description:   
Type:          INTEGER
Size:          10

     State Variable #6
Name:          RATIO
Description:   
Type:          REAL
Size:          6

     State Variable #7
Name:          WAIT
Description:   
Type:          REAL
Size:          1000



          VERTICES
          --------

     Vertex #1
Name:             INIT
Description:      
State Changes:    SERVER[0]=2,SERVER[1]=1,QUEUE[0]=0,QUEUE[1]=0,ID[0]=-1,ID[1]=0,ID[2]=0,ID[3]=0,ID[4]=0,ID[5]=0,ID[6]=0,ID[7]=0,RATIO[0]=0,RATIO[1]=0,RATIO[2]=0,ID[9]=0,RATIO[3]=0,RATIO[4]=0,RATIO[5]=0
Parameter(s):     
Bitmap(Inactive): 
Bitmap(Active):   
Use Flowchart Shapes:   0
Use Opaque Bitmaps:   0
Location:         X: -0.88;  Y:  2.34;  Z: -1.00;
Local Trace:      
Trace Location:   Bottom

     Vertex #2
Name:             ARR
Description:      Arrival of customers into the system
State Changes:    ID[0]=ID[0]+1,QUEUE[0]=QUEUE[0]+1,SYSTEM[ID[0]]=CLK,RATIO[1]=RATIO[1]+CLK*(QUEUE[0]==8&RATIO[2]==0),RATIO[2]=(QUEUE[0]>7),RATIO[4]=RATIO[4]+CLK*(QUEUE[0]==4&RATIO[5]==0),RATIO[5]=(QUEUE[0]>3),WAIT[ID[0]]=CLK
Parameter(s):     
Bitmap(Inactive): 
Bitmap(Active):   
Use Flowchart Shapes:   0
Use Opaque Bitmaps:   0
Location:         X: -0.88;  Y:  1.87;  Z: -1.00;
Local Trace:      
Trace Location:   Bottom

     Vertex #3
Name:             TOPPING
Description:      Begin process of creating pizza.
State Changes:    QUEUE[0]=QUEUE[0]-1,SERVER[0]=SERVER[0]-1,ID[2]=ID[2]+1,SERVICE[ID[1]]=CLK,RATIO[0]=RATIO[0]+(CLK-RATIO[1])*(QUEUE[0]==7),RATIO[1]=RATIO[1]*(QUEUE[0]!=7),RATIO[2]=(RATIO[1]!=0),RATIO[3]=RATIO[3]+(CLK-RATIO[4])*(QUEUE[0]==3),RATIO[4]=RATIO[4]*(QUEUE[0]!=3),RATIO[5]=(RATIO[4]!=0),WAIT[ID[1]]=CLK-WAIT[ID[1]]
Parameter(s):     ID[1]
Bitmap(Inactive): 
Bitmap(Active):   
Use Flowchart Shapes:   0
Use Opaque Bitmaps:   0
Location:         X: -0.22;  Y:  1.87;  Z: -1.00;
Local Trace:      
Trace Location:   Bottom

     Vertex #4
Name:             COOK
Description:      Start baking the pizza
State Changes:    SERVER[0]=SERVER[0]+1,SERVICE[ID[3]]=CLK-SERVICE[ID[3]]
Parameter(s):     ID[3]
Bitmap(Inactive): 
Bitmap(Active):   
Use Flowchart Shapes:   0
Use Opaque Bitmaps:   0
Location:         X:  0.54;  Y:  1.87;  Z: -1.00;
Local Trace:      
Trace Location:   Bottom

     Vertex #5
Name:             READY
Description:      Pizza is out of the oven
State Changes:    QUEUE[1]=QUEUE[1]+1,ID[9]=(ID[4]!=ID[6])*(ID[4]*(QUEUE[1]==1))
Parameter(s):     ID[4]
Bitmap(Inactive): 
Bitmap(Active):   
Use Flowchart Shapes:   0
Use Opaque Bitmaps:   0
Location:         X:  1.23;  Y:  1.87;  Z: -1.00;
Local Trace:      
Trace Location:   Bottom

     Vertex #6
Name:             FINISH
Description:      Finishing touches on pizza (extra toppings and boxing)
State Changes:    QUEUE[1]=QUEUE[1]-1,SERVER[1]=SERVER[1]-1,ID[6]=ID[6]+1,ID[9]=0
Parameter(s):     ID[5]
Bitmap(Inactive): 
Bitmap(Active):   
Use Flowchart Shapes:   0
Use Opaque Bitmaps:   0
Location:         X:  1.22;  Y:  1.47;  Z: -1.00;
Local Trace:      
Trace Location:   Bottom

     Vertex #7
Name:             DELIVER
Description:      Deliver pizza to the customer
State Changes:    SERVER[1]=SERVER[1]+1,SYSTEM[ID[7]]=CLK-SYSTEM[ID[7]]
Parameter(s):     ID[7]
Bitmap(Inactive): 
Bitmap(Active):   
Use Flowchart Shapes:   0
Use Opaque Bitmaps:   0
Location:         X:  1.22;  Y:  0.95;  Z: -1.00;
Local Trace:      
Trace Location:   Bottom

     Vertex #8
Name:             STOP
Description:      
State Changes:    
Parameter(s):     
Bitmap(Inactive): 
Bitmap(Active):   
Use Flowchart Shapes:   0
Use Opaque Bitmaps:   0
Location:         X: -0.22;  Y:  2.34;  Z: -1.00;
Local Trace:      
Trace Location:   Bottom



          EDGES
          -----


     Graphics Edge #1

  Sub-Edge #1
Description:   Initialization event
Type:          Scheduling
Origin:        INIT
Destination:   ARR
Condition:     1==1
Delay:         -2.4966*LN{1-RND}
Priority:      5
Attributes:    

     Graphics Edge #2

  Sub-Edge #2
Description:   Start creating pizza if server is available
Type:          Scheduling
Origin:        ARR
Destination:   TOPPING
Condition:     SERVER[0]>0&QUEUE[0]>0
Delay:         0
Priority:      5
Attributes:    ID[0]

     Graphics Edge #3

  Sub-Edge #3
Description:   Schedule end of creation
Type:          Scheduling
Origin:        TOPPING
Destination:   COOK
Condition:     1==1
Delay:         0.3666+2.6334*RND
Priority:      6
Attributes:    ID[1]

  Sub-Edge #4
Description:   Schedule another pizza creation if queue is not empty.
Type:          Scheduling
Origin:        COOK
Destination:   TOPPING
Condition:     QUEUE[0]>0
Delay:         0
Priority:      5
Attributes:    ID[2]

     Graphics Edge #4

  Sub-Edge #5
Description:   Baking the pizza
Type:          Scheduling
Origin:        COOK
Destination:   READY
Condition:     1==1
Delay:         2.9333+3*RND
Priority:      5
Attributes:    ID[3]

     Graphics Edge #5

  Sub-Edge #6
Description:   If server is available, finish pizza for delivery
Type:          Scheduling
Origin:        READY
Destination:   FINISH
Condition:     SERVER[1]>0&QUEUE[1]>0
Delay:         0
Priority:      5
Attributes:    ID[4]

     Graphics Edge #6

  Sub-Edge #7
Description:   Complete finishing touches
Type:          Scheduling
Origin:        FINISH
Destination:   DELIVER
Condition:     1==1
Delay:         -0.9494*LN{1-RND}
Priority:      6
Attributes:    ID[5]

  Sub-Edge #8
Description:   Start finishing next pizza if pizza is waiting.
Type:          Scheduling
Origin:        DELIVER
Destination:   FINISH
Condition:     QUEUE[1]>0
Delay:         0
Priority:      5
Attributes:    ID[6]*(ID[9]==0)+(ID[9]!=0)*ID[9]

     Graphics Edge #7

  Sub-Edge #9
Description:   Arrival event
Type:          Scheduling
Origin:        ARR
Destination:   ARR
Condition:     1==1
Delay:         -2.4966*LN{1-RND}*(CLK<50|(CLK>80&CLK<110)|CLK>140)+-0.7444*LN{1-RND}*((CLK>=50&CLK<=80)|(CLK>=110&CLK<=140))
Priority:      5
Attributes:    

     Graphics Edge #8

  Sub-Edge #10
Description:   
Type:          Scheduling
Origin:        INIT
Destination:   STOP
Condition:     1==1
Delay:         180
Priority:      5
Attributes:    

     Graphics Edge #9

  Sub-Edge #11
Description:   
Type:          Cancelling
Origin:        STOP
Destination:   ARR
Condition:     1==1
Delay:         0
Priority:      5
Attributes:    

