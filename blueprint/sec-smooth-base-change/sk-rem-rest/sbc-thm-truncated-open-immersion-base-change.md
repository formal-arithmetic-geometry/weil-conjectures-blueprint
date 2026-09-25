+++
id = "sbc-thm-truncated-open-immersion-base-change"
kind = "theorem"
title = "Base change for open immersions under local acyclicity"
order = 1465
uses = ["lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-torsion-filtered-union", "sbc-def-local-acyclicity", "sbc-def-milnor-tube", "sbc-def-specialization-map", "sbc-def-strict-localization", "sbc-def-universal-local-acyclicity", "sbc-lem-strict-henselian-constant-cohomology", "sbc-thm-smooth-base-change"]
+++
Let $j:U\hookrightarrow Z$ be a quasi-compact open immersion, let
$a:Z'\to Z$ be
universally locally
acyclic, and form the Cartesian square

$$
\begin{array}{ccc}
U' & \xrightarrow{\;a_U\;} & U\\
j'\big\downarrow & & \big\downarrow j\\
Z' & \xrightarrow{\;a\;} & Z.
\end{array}
$$

Let $F$ be a sheaf on $U_{\Et}$ whose geometric stalks are torsion of
orders invertible on $Z'$. Then

$$
a^{-1}R^qj_*F\xrightarrow{\ \sim\ }R^qj'_*a_U^{-1}F
$$

for every $q\geq0$, natural in $F$ and compatible with composition of
open immersions and with further base change. (This is the classical
base change for open immersions under local acyclicity, given by the
Deligne specialization-map argument of SGA 4.5; it is recorded here for
the use of the smooth-base-change chapter, and is not needed for the proof of
[sbc-thm-smooth-base-change].)

## Proof

The assertion is local on $Z$ for the etale topology; by the filtered
torsion reduction of [lemma-weil-pbc-torsion-filtered-union] we may
assume $F$ killed by one integer invertible on $Z'$, and after an
etale covering and by the finite stalk formula of
[lemma-weil-pbc-finite-stalk-formula] we may assume $F$ finite
locally constant, hence constant equal to $\underline A$ for a finite
group $A$ of order invertible on $Z'$ after a further etale covering.
For a geometric point $\bar z'$ of $Z'$ with image
$\bar z=a(\bar z')$, the stalk of the base-change map at $\bar z'$ is
the restriction map of the strict localizations of
[sbc-def-strict-localization],

$$
H^q\bigl(U\times_ZZ_{(\bar z)},F\bigr)
\longrightarrow H^q\bigl(U'\times_{Z'}Z'_{(\bar z')},F\bigr),
$$

which, after base changing the whole square by $Z_{(\bar z)}\to Z$ and
using the Milnor tube $M_a(\bar z,\bar t)$ of
[sbc-def-milnor-tube] (with $\bar t$ the geometric point
$Z'_{(\bar z')}\to Z_{(\bar z)}$), is identified by the
specialization map of [sbc-def-specialization-map]: the source is
$A$ in degree $0$ and $0$ above by strict henselianity
([sbc-lem-strict-henselian-constant-cohomology]), and by the local
acyclicity of every base change of $a$
([sbc-def-local-acyclicity] and
[sbc-def-universal-local-acyclicity]) the cohomology of the tube
$M_a(\bar z,\bar t)$ is $A$ in degree $0$ and $0$ above; the
specialization map is therefore an isomorphism in every degree, and
geometric stalks are conservative for the sheaves $a^{-1}R^qj_*F$ and
$R^qj'_*a_U^{-1}F$, so this is the isomorphism. Naturality and the
compatibility with compositions and base changes are the functoriality
of the defining composites.
