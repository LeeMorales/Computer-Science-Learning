var
 m:array[1..4,1..6] of real ;
 i,j:longint;
begin
  for i:=1 to 4 do m[i,5]:=0;
  for i:=1 to 4 do
     for j:=1 to 4 do
       begin
         read(m[i,j]);
         m[1,5]:=m[i,5]+m[i,j];
       end;
  for i:=1 to 4 do
   begin
     for j:=1 to 5 do
       write(m[i,j]:8:1);
   writeln;
   end;
end.

