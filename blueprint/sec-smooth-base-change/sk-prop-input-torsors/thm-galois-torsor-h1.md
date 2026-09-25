+++
id = "thm-galois-torsor-h1"
kind = "theorem"
title = "Torsors and first etale cohomology"
order = 1408
uses = ["def-galois-categories", "def-weil-pbc-etale-cohomology", "def-weil-pbc-finite-torsors", "lem-galois-flasque", "thm-galois-lc-etale"]
+++
In the situation of [def-galois-categories], let $M$ be a finite
abelian group. Then the construction below is a canonical bijection

$$
\operatorname{Tor}^1(Y,M)\xrightarrow{\ \sim\ }H^1(Y_{\Et},\underline M),
$$

natural in $(Y,M)$. For a curve the statement is proved independently in
the smooth-curve chapter by $\operatorname{Ext}^1$ and the Baer-sum
description of torsors.

## Proof

We use the $M$-torsors of [def-weil-pbc-finite-torsors], the
cohomology $H^1(Y_{\Et},-)$ of [def-weil-pbc-etale-cohomology]
and the dictionary of [thm-galois-lc-etale] between finite locally
constant sheaves and finite etale schemes.
Step 1: the lifting torsor. Choose $0\to\underline M\to I\xrightarrow{d}J\to0$ as in [lem-galois-flasque] and let $s\in J(Y)$ represent a class in $H^1(Y_{\Et},\underline M)$. Define
$P_s(U)=\{x\in I(U):d(x)=s|_U\}$, a sheaf of sets with the translation
action of $\underline M$.
Step 2: $P_s$ is an $M$-torsor. If $x,x'\in P_s(U)$ then
$d(x-x')=0$, so $x'-x\in\ker d(U)=\underline M(U)$; hence
$M\times P_s\to P_s\times P_s$, $(m,x)\mapsto(x+m,x)$, is an
isomorphism. It is locally nonempty because $J$ is the quotient sheaf of
$I$: over a cover $\{U_i\}$ there are $x_i\in I(U_i)$ with
$d(x_i)=s|_{U_i}$, and then $P_s|_{U_i}\cong\underline M|_{U_i}$. So
$P_s$ is finite locally constant with simply transitive $M$-action,
i.e. an $M$-torsor.
Step 3: well-definedness and naturality. Translation by $x\in I(Y)$
identifies $P_{s+d(x)}\cong P_s$, so $s\mapsto[P_s]$ factors through
$\operatorname{coker}(d_Y)\cong H^1(Y_{\Et},\underline M)$; functoriality
of $I,J,d$ and of pullback gives naturality.
Step 4: injectivity. Suppose $P_s\cong P_{s'}$. Trivialize both over a
cover $\{U_i\}$ and choose $p_i\in P_s(U_i)$, $p_i'\in P_{s'}(U_i)$.
Over $U_i$ the isomorphism is translation by $a_i=p_i'-p_i\in I(U_i)$;
over $U_{ij}$ the two trivializations differ by an element of
$\underline M(U_{ij})$, and compatibility of the isomorphism with the
torsor structures says exactly that the $a_i$ agree on overlaps, so they
glue to $a\in I(Y)$ with $d(a)=s'-s$. Hence $s-s'\in \operatorname{im}(d_Y)$ and the classes agree.
Step 5: surjectivity. Let $P$ be an $M$-torsor and trivialize it over
a cover $\{U_i\to Y\}$ with sections $p_i\in P(U_i)$ (possible by
Step 2 applied to the locally constant structure); put
$c_{ij}=p_i-p_j\in\underline M(U_{ij})$. The $c_{ij}$ form a Čech
1-cocycle. The standard exact sequence of Čech complexes
$0\to\check C^\bullet(\mathcal U,\underline M)\to C^\bullet(\mathcal U,I)\to C^\bullet(\mathcal U,J)\to0$ has a long exact
cohomology sequence — the five-term exact sequence of the Čech
double complex, a computation in homological algebra — which identifies
$\check H^1(\mathcal U,\underline M)$ with the classes in
$H^1(Y_{\Et},\underline M)$ whose restrictions to the $U_i$ vanish; the
class $\alpha$ of the cocycle is such a class. Both $P$ and the lifting
torsor $P_s$ for a representative $s$ of $\alpha$ are built from the
same trivializations and the same glueing data, so $P\cong P_s$.
Steps 1–5 give the bijection.
