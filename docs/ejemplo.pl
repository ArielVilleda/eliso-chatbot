print "Hola, soy Eliso, ¿cómo te llamas?\n";
$nombre = <STDIN>;
chomp $nombre;
print "Mucho gusto, $nombre, ¿en qué te puedo ayudar?\n";

while (not $parar) {
   $entrada = <STDIN>;
   chomp $entrada;

   if ($entrada =~ /papá|padre|madre|hermano|hermana/) {
      print "Cuéntame más de tu familia\n";
   }
   elsif ($entrada =~ /estoy (.*)/) {
      print "¿Por qué estás $1\n";
   }
   elsif ($entrada =~ /^adiós/) {
      print "Espero haberte ayudado. ¡Hasta luego!\n";
      $parar=1;
   }
   elsif (rand > 0.5) {
      $entrada =~ s/\bcomo\b/comes/g;
      $entrada =~ s/\bhablo\b/hablas/g;
      $entrada =~ s/\bveo\b/ves/g;
      $entrada =~ s/\bescucho\b/escuchas/g;
      $entrada =~ s/\boigo\b/oyes/g;
      $entrada =~ s/\btengo\b/tienes/g;
      $entrada =~ s/\bcorro\b/corres/g;
      $entrada =~ s/\bcamino\b/caminas/g;
      $entrada =~ s/\bestoy\b/estás/g;
      $entrada =~ s/\bsoy\b/eres/g;
      $entrada =~ s/\bmuero\b/mueres/g;
      $entrada =~ s/\bvivo\b/vives/g;
      $entrada =~ s/\bcambio\b/cambias/g;
      $entrada =~ s/\bsiento\b/sientes/g;
      $entrada =~ s/\bpuedo\b/puedes/g;
      $entrada =~ s/\bmi\b/tu/g;
      $entrada =~ s/\bmí\b/ti/g;
      $entrada =~ s/\bme\b/te/g;
      $entrada =~ s/\byo\b/tú/g;

      if (rand > 0.5) {
          print "¿Por qué $entrada?\n";
      }
      else {
          print "Así que $entrada...\n";
      }
   }
   else {
      if (rand > 0.5) {
         print "Cuéntame más...\n";
      }
      else {
         print "No me digas!\n";
      }
   }
}
