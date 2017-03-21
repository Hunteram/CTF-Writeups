import binascii

#Gathered from connecting manually
# m = 1, r = 1
g = 76148136246979412868353192826161253341403849263254887278017187958514513340458179944731332795505616407225022188597713956679924138156737337560391522285190471306102238935856085554943425316921717217530405444795878376547349107664015741971592178799088766898531556269231518219697725522509132047243753064371633643298

# m = 2, r = 1
g2 = 152296272493958825736706385652322506682807698526509774556034375917029026680916359889462665591011232814450044377195427913359848276313474675120783044570380942612204477871712171109886850633843434435060810889591756753094698215328031483943184357598177533797063112538463036439395451045018264094487506128743267286595

expectedG2 = g*g

#Using Factordb, we find that expectedG2-g2 is a perfect square of a prime, which is below
#http://factordb.com/index.php?id=1100000000882961502
n = 76148136246979412868353192826161253341403849263254887278017187958514513340458179944731332795505616407225022188597713956679924138156737337560391522285190471306102238935856085554943425316921717217530405444795878376547349107664015741971592178799088766898531556269231518219697725522509132047243753064371633643297
n2 = n*n
m2r2 = 642704871773304452155778596282877892451871980828477596157415930594972102473171707034871466334408214634990379265334519095544245651795310239071984348465353456082430791507322024283077057140015173791209040404351064470318177893091562745760770981747716308255111472933684059218100124906239297276402113587510274467857526915676715307055889593001002210535184406398178516901311847346979934161946287183599368736554797730366291587740218078384204696550286009123986874335424671114430592617561047352470044247529967986001239137580719442869043114141323570567593427242451750466586033713111304296116982128148631354597378733690535403149
#check for no errors
assert (pow(g,2,n2)*pow(2,n,n2))%n2 == m2r2
assert (pow(g,2,n2))%n2 == g2

# get int of string easyctf{3ncrypt_m3!}
goal = b'easyctf{3ncrypt_m3!}'
hexGoal = str(binascii.hexlify(goal),'utf-8')
goal = int(hexGoal,16)
#print(goal)
#goal is divisible by 5, so use that for Homomorphic property
m5r1 = pow(g,5,n2)
goalDiv5 = goal // 5
# Now use the Homomorphic property :)
flagInt = pow(m5r1,goalDiv5,n2)
print(flagInt)
