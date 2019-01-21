var
  a:array[0..9] of longint;
  i,g,s,b,k,t:longint;
begin
  for i:=100 to 333 do
    begin
        for k:=0 to 9 do
         a[k]:=0;
         k:=i;
         g:=k mod 10;
         b:=k div 100;
         s:=(k div 10) mod 10;
         a[g]:=1;
         a[s]:=1;
         a[b]:=1;
         k:=2*i;
         g:=k mod 10;
         b:=k div 100;
         s:=(k div 10) mod 10;
         a[g]:=1;
         a[s]:=1;
         a[b]:=1;
         k:=3*i;
         g:=k mod 10;
         b:=k div 100;
         s:=(k div 10) mod 10;
         a[g]:=1;
         a[s]:=1;
         a[b]:=1;
         t:=0;
         for k:=1 to 9 do
           t:=t+a[k];
         if t=9 then writeln(i:4,i*2:4,i*3:4);
     end;
end.
