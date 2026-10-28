+++
kind  = "proof"
of    = "lem-sfb-dc-open-lower-shriek-preserves"
uses = ["sk-def-sfb-constructible"]
+++
The extension by zero $j_!$ on module objects is exact ([det-def-sfb-module-lower-shriek]). So
$H^q(D(j_!)K)\cong j_!H^q(K)$, and $D(j_!)K$ is bounded. Let $M$ be a constructible
$\Lambda_U$-module ([sk-def-sfb-constructible]) with finite stratification $U=\bigsqcup_aU_a$
such that each $M|_{U_a}$ is locally finitely presented. Each $U_a$ is locally closed in $X$, since
$U$ is open. So the $U_a$ together with the reduced closed complement $X\setminus U$ form a
finite stratification of $X$. On $U_a$ the restriction of $j_!M$ is $M|_{U_a}$, because
$j^*j_!\cong\mathrm{id}$. On $X\setminus U$ it is $0$, which is finitely presented. Hence $j_!M$
is constructible.
