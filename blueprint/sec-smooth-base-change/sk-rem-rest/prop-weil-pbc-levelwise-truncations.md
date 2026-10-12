+++
id = "prop-weil-pbc-levelwise-truncations"
kind = "theorem"
title = "Levelwise truncations of the adic tower"
order = 1429
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-site-comparison-morphism"]
tags = ["latex:proposition"]
+++
Let the adic datum be $A=\mathcal O_E$, $I=(\varpi)$, with $P_n=A_{E,n}$,
and let $K_\bullet\in D(\operatorname{Tow}_A(T))$ be an adic tower (an
object with normalization isomorphisms
$K_{n+1}\otimes^L_{P_{n+1}}P_n\xrightarrow{\sim}K_n$ satisfying the quotient
cocycle), given by a K-flat representative $QK$ of a single object $K$ of
the underlying pro-etale complex category, $K_n=QK\otimes^L_{A_T}(P_n)_T$.
Then for every $m\in\mathbf Z$:

1. the levelwise truncations
   $$
    \tau^{\le m}K_\bullet:=(\tau^{\le m}K_n)_n,\qquad
    \tau^{\ge m+1}K_\bullet:=(\tau^{\ge m+1}K_n)_n,
   $$
   of the levelwise t-structure of $D(\operatorname{Tow}_A(T))$ (whose
   evaluations are the levelwise canonical truncations of the strict-tower
   representatives) are adic towers, with canonical normalization
   isomorphisms
   $$
    \tau^{\le m}K_{n+1}\otimes^L_{P_{n+1}}P_n
    \xrightarrow{\sim}\tau^{\le m}K_n,\qquad
    \tau^{\ge m+1}K_{n+1}\otimes^L_{P_{n+1}}P_n
    \xrightarrow{\sim}\tau^{\ge m+1}K_n
   $$
   satisfying the quotient cocycle, *provided* the following
   Tor-compatibility condition (1) holds: for every $n$ and every $q\ge m+1$
   the canonical morphism
   $$
    \mathcal H^q(K_{n+1})\otimes^L_{P_{n+1}}P_n
    \longrightarrow\mathcal H^q(K_n)
   $$
   is an isomorphism;
2. if $K_\bullet$ is uniformly bounded constructible, with local models
   $L_{\alpha j}$ supported in $[d_0,d_1]$ and with the isomorphisms
   $K_n|_{U_{\alpha j}}\simeq L_{\alpha j}\otimes^L_{A_T}(P_n)_T$ for every
   $n$, then $\tau^{\le m}K_\bullet$ is uniformly bounded constructible with
   the local models $\tau^{\le m}L_{\alpha j}$ (supported in
   $[\min(d_0,m),m]$), and $\tau^{\ge m+1}K_\bullet$ is uniformly bounded
   constructible with the local models
   $$
    C_{\alpha j}:=\operatorname{Cone}\bigl(\tau^{\le m}L_{\alpha j}
    \longrightarrow L_{\alpha j}\bigr)
   $$
   (supported in $[m+1,d_1]$), the terms of both families of models being
   finite locally free and their reductions having finite lisse cohomology;
3. for every $n$ there are canonical isomorphisms
   $$
    \mathcal H^i\bigl((\tau^{\le m}K_\bullet)_n\bigr)
     \xrightarrow{\sim}\mathcal H^i(K_n)\quad(i\le m),
    \qquad
    \mathcal H^i\bigl((\tau^{\le m}K_\bullet)_n\bigr)=0\quad(i>m),
   $$
   and analogously
   $$
    \mathcal H^i\bigl((\tau^{\ge m+1}K_\bullet)_n\bigr)
     \xrightarrow{\sim}\mathcal H^i(K_n)\quad(i\ge m+1),
    \qquad
    \mathcal H^i\bigl((\tau^{\ge m+1}K_\bullet)_n\bigr)=0\quad(i\le m),
   $$
   compatible with the normalization maps; if the tower carries compatible
   etale-origin witnesses [def-weil-pbc-etale-origin-witness]
   $(L_n^{\mathrm{et}},\alpha_n)$, the truncated towers carry the
   compatible witnesses
   $(\tau^{\le m}L_n^{\mathrm{et}},\nu^*\tau^{\le m}\circ\alpha_n)$ and
   $(\tau^{\ge m+1}L_n^{\mathrm{et}},\nu^*\tau^{\ge m+1}\circ\alpha_n)$.

Statements (i) and (ii) are asserted under the Tor-compatibility
condition (1); statement (iii) holds unconditionally, being a formal
property of the canonical truncations.

Since $\mathcal H^q(K_{n+1})\otimes^L_{P_{n+1}}P_n$ has cohomology
$\operatorname{Tor}_p^{P_{n+1}}(\mathcal H^q(K_{n+1}),P_n)$ in degree $-p$,
condition (1) says that for $q\ge m+1$ the higher Tor terms
$\operatorname{Tor}_p^{P_{n+1}}(\mathcal H^q(K_{n+1}),P_n)$, $p\ge1$, vanish
and $\mathcal H^q(K_{n+1})\otimes_{P_{n+1}}P_n\to\mathcal H^q(K_n)$ is an
isomorphism; these Tor terms are the Künneth obstruction in the spectral
sequence
$$
 E_2^{p,q}=\operatorname{Tor}_p^{P_{n+1}}
 \bigl(\mathcal H^q(K_{n+1}),P_n\bigr)\Rightarrow
 \mathcal H^{q-p}(K_n)
$$
of the reduction morphism. A sufficient condition is that the cohomology
sheaves $\mathcal H^i(K)$ of the ambient object (equivalently, of the local
models) be $\varpi$-torsion-free (over the discrete valuation ring $A_T$
equivalently flat) for all $i\ge m+1$, because then
$\mathcal H^q(K_{n+1})=\mathcal H^q(K)\otimes^L_{A_T}(P_{n+1})_T$ has no
higher $\varpi$-torsion and the morphism of (1) is the identity on
$(\mathcal H^q(K)/\varpi^{n+1})\otimes^L_{P_{n+1}}P_n$.

*In general the levelwise truncations are not adic towers*: the failure
is exactly the Tor-contribution. For instance, for
$K=(A_T/\varpi)[-(m+1)]$ (a single shift of the constant
$\varpi$-torsion sheaf) one has
$$
 K_n=K\otimes^L_{A_T}(P_n)_T
 =\bigl((A_T/\varpi)\oplus(A_T/\varpi)[1]\bigr)[-(m+1)]
$$
for every $n\ge1$ — the two-term Koszul resolution of $(P_n)_T$ over
$A_T$ gives
$\operatorname{Tor}_1^{A_T}(A_T/\varpi,(P_n)_T)=A_T/\varpi$ — and hence
$\tau^{\le m}K_n=(A_T/\varpi)[-m]$ for every $n$, whereas
$$
 (\tau^{\le m}K_{n+1})\otimes^L_{P_{n+1}}P_n
 =\bigl((A_T/\varpi)\otimes^L_{P_{n+1}}P_n\bigr)[-m],
$$
whose cohomology is $A_T/\varpi$ in *every* degree $\le m$ (since
$\operatorname{Tor}_i^{P_{n+1}}(A_T/\varpi,P_n)=A_T/\varpi$ for all
$i\ge0$, $n\ge1$); this is not $(A_T/\varpi)[-m]$, so the levelwise
truncated tower $\tau^{\le m}K_\bullet$ fails to be an adic tower.

*Local freeness of the terms of a model does not imply (1)*: for the
two-term complex $P_{n+1}\xrightarrow{\ \varpi\ }P_{n+1}$ the terms are
free while the first cohomology is the torsion module $P_n$, so freeness of
the terms forces neither torsion-freeness of the cohomology nor the
vanishing of the higher Tor terms in (1). Flatness of the cohomology
sheaves of the local models is strictly stronger than finiteness of their
terms.
