var
 i,n,s,a,b,c:longint;
 begin
  read(n);
  a:=n div 100;
  c:=n mod 10;
  if a=c then
             begin
               for i:=1 to 10000 do
               if  n mod i=0 then s:=s+1;
               if s=2 then write('yes!')
                      else write('bu shi zhi shu,shi hui wen shu!')
             end
                      else writeln('e.......');
end.

