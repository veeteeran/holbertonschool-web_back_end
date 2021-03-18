#
!
/
u
s
r
/
b
i
n
/
p
y
t
h
o
n
3


"
"
"
 
B
a
s
e
C
a
c
h
i
n
g
 
m
o
d
u
l
e


"
"
"




c
l
a
s
s
 
B
a
s
e
C
a
c
h
i
n
g
(
)
:


 
 
 
 
"
"
"
 
B
a
s
e
C
a
c
h
i
n
g
 
d
e
f
i
n
e
s
:


 
 
 
 
 
 
-
 
c
o
n
s
t
a
n
t
s
 
o
f
 
y
o
u
r
 
c
a
c
h
i
n
g
 
s
y
s
t
e
m


 
 
 
 
 
 
-
 
w
h
e
r
e
 
y
o
u
r
 
d
a
t
a
 
a
r
e
 
s
t
o
r
e
d
 
(
i
n
 
a
 
d
i
c
t
i
o
n
a
r
y
)


 
 
 
 
"
"
"


 
 
 
 
M
A
X
_
I
T
E
M
S
 
=
 
4




 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
 
I
n
i
t
i
l
i
a
z
e


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
s
e
l
f
.
c
a
c
h
e
_
d
a
t
a
 
=
 
{
}




 
 
 
 
d
e
f
 
p
r
i
n
t
_
c
a
c
h
e
(
s
e
l
f
)
:


 
 
 
 
 
 
 
 
"
"
"
 
P
r
i
n
t
 
t
h
e
 
c
a
c
h
e


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
p
r
i
n
t
(
"
C
u
r
r
e
n
t
 
c
a
c
h
e
:
"
)


 
 
 
 
 
 
 
 
f
o
r
 
k
e
y
 
i
n
 
s
o
r
t
e
d
(
s
e
l
f
.
c
a
c
h
e
_
d
a
t
a
.
k
e
y
s
(
)
)
:


 
 
 
 
 
 
 
 
 
 
 
 
p
r
i
n
t
(
"
{
}
:
 
{
}
"
.
f
o
r
m
a
t
(
k
e
y
,
 
s
e
l
f
.
c
a
c
h
e
_
d
a
t
a
.
g
e
t
(
k
e
y
)
)
)




 
 
 
 
d
e
f
 
p
u
t
(
s
e
l
f
,
 
k
e
y
,
 
i
t
e
m
)
:


 
 
 
 
 
 
 
 
"
"
"
 
A
d
d
 
a
n
 
i
t
e
m
 
i
n
 
t
h
e
 
c
a
c
h
e


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
a
i
s
e
 
N
o
t
I
m
p
l
e
m
e
n
t
e
d
E
r
r
o
r
(
"
p
u
t
 
m
u
s
t
 
b
e
 
i
m
p
l
e
m
e
n
t
e
d
 
i
n
 
y
o
u
r
 
c
a
c
h
e
 
c
l
a
s
s
"
)




 
 
 
 
d
e
f
 
g
e
t
(
s
e
l
f
,
 
k
e
y
)
:


 
 
 
 
 
 
 
 
"
"
"
 
G
e
t
 
a
n
 
i
t
e
m
 
b
y
 
k
e
y


 
 
 
 
 
 
 
 
"
"
"


 
 
 
 
 
 
 
 
r
a
i
s
e
 
N
o
t
I
m
p
l
e
m
e
n
t
e
d
E
r
r
o
r
(
"
g
e
t
 
m
u
s
t
 
b
e
 
i
m
p
l
e
m
e
n
t
e
d
 
i
n
 
y
o
u
r
 
c
a
c
h
e
 
c
l
a
s
s
"
)
