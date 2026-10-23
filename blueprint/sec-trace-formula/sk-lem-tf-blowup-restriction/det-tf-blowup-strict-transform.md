+++
id = "det-tf-blowup-strict-transform"
kind = "lemma"
title = "Strict transform of the test curve"
order = 3526
uses = ["det-tf-blowup-configuration"]
+++
In the situation of [det-tf-blowup-configuration], let $B$ be a reduced
closed curve through $t$ with $C_tD\cap C_tB=\{0\}$, and let $B'$ be its
strict transform. Then $B'$ is finite over $B$ and is a finite disjoint
union

$$
 B'=\coprod_{s\in B'\cap P}B'_s
$$

of strictly local curves $B'_s$ with closed point $s$. Each $s$ lies in
$Y$, each $B'_s$ is a closed curve in $Z$ with $B'_s\cap Y=\{s\}$, equal
to its own strict localization at $s$, and $f$ induces

$$
 B-t\simeq B'-P=\coprod_s\,(B'_s-s).
$$

Consequently, for every complex $F$ on $T-D$, the restriction map
$R\Gamma(T-D,F)\to R\Gamma(B-t,F|_{B-t})$ is identified with the direct
sum of the restriction maps
$R\Gamma(Z-Y,f^*F)\to R\Gamma(B'_s-s,f^*F|_{B'_s-s})$.
