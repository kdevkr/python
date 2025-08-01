.z.K / release version
.z.l / license info



size:1000
r:size?`A`B`C`D
t:size?.z.p
v:size?123.456
tbl:flip `r`t`v!(r;t;v)
tbl

.auto.gc:{
    is0:00:00:00=1000 xbar .z.t;
    if[is0; (-1 ".Q.gc[]";.Q.gc[]); 0b];
 }


.z.ts:{
    -1 "[.z.ts]: ",string[`datetime$.z.p]," timer";
    .auto.gc[];
 }

/ equals system "t"
\t
\t 1000
