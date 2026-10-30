+++
kind  = "proof"
of    = "lem-integral-ctf-equals-bc"
uses = ["det-def-sfb-constructible-local-model", "def-weil-open-closed-recollement", "def-weil-finite-tor-amplitude"]
+++
For $\Lambda=\cO_E$ the equality $\Dctf=\Dbc$ is also the equivalence (3)$\Leftrightarrow$(4) of the
integral constructibility criterion, see [sk-prop-integral-criterion]. In general we argue with the local
models. The scalar ring $\Lambda(*)$ is the discrete valuation ring $\cO_E$ or the field $E$ or $\Qlb$.

*Local models.* A finitely presented $\Lambda(*)$-module $P$ has a finite projective resolution
$0\to\Lambda(*)^m\xrightarrow{A}\Lambda(*)^n\to P\to0$, of length at most one over the discrete valuation
ring and of length zero over a field. Pulling it back along $\Lambda(*)\to\Lambda_U$ is exact: over a field
every module is flat, and $\cO_{E,U}$ is flat over the constant sheaf $(\cO_E)_U$ \stacks{099L}. So a module
with a finite constant local model ([det-def-sfb-constructible-local-model]) is, on each member $U_i$ of the
cover, quasi-isomorphic to $[\Lambda_{U_i}^m\to\Lambda_{U_i}^n]$ in degrees $[-1,0]$, a complex of flat
modules; its derived tensor product with any $N$ is $[N^m\to N^n]$, with cohomology in $[-1,0]$; over a
field one may take $m=0$, and then the cohomology is in degree $0$.

*Locality.* Restriction to the members of a pro-étale cover is exact, commutes with $\otimes^{\mathbf L}$,
and is jointly conservative; so Tor amplitude may be checked on a cover.

*Strata.* Let $M$ be constructible, with a finite stratification. Choose an open stratum
$j\colon U\hookrightarrow X$ with closed complement $i\colon Z\hookrightarrow X$ a union of strata, and
induct on the number of strata. The localization sequence $0\to j_!j^*M\to M\to i_*i^*M\to0$
([def-weil-open-closed-recollement]) and the projection formulas
$(j_!B)\otimes^{\mathbf L}N=j_!(B\otimes^{\mathbf L}j^*N)$ and
$(i_*C)\otimes^{\mathbf L}N=i_*(C\otimes^{\mathbf L}i^*N)$ (both sides are computed by flat resolutions, and
$j_!$, $i_*$, $j^*$, $i^*$ are exact) reduce (1) to $j^*M$ and to $i^*M$, and by induction to a single
stratum, where it is the local model computation.

*Complexes.* For $K\in\Dbc(X,\Lambda)$ with cohomology in $[a,b]$, induct on $b-a$ with the truncation
triangles $\tau_{<b}K\to K\to H^b(K)[-b]\to$. Tor amplitude is stable under shifts and extensions
([def-weil-finite-tor-amplitude]), so (1) gives Tor amplitude in $[a-1,b]$, and in $[a,b]$ when $\Lambda$
is a field, by the $[0,0]$ case of (1). In the field case this says: on each stratum $a\colon S\hookrightarrow X$
the module is lisse, i.e. locally free of finite rank, hence flat, and with $a=i\circ u$ the projection
formulas give $a_!L\otimes^{\mathbf L}_{\Lambda_X}M\cong a_!(L\otimes_{\Lambda_S}a^*M)$, a sheaf in degree
$0$. Thus $\Dbc\subseteq\Dctf$; the
reverse inclusion is the definition.

*The examples.* Over $A=\mathbf Z/\ell^2$, the module $\mathbf F_\ell$ has the infinite periodic resolution
$\cdots\xrightarrow{\ell}A\xrightarrow{\ell}A\to\mathbf F_\ell$, and
$\operatorname{Tor}^A_q(\mathbf F_\ell,\mathbf F_\ell)=\mathbf F_\ell$ for all $q\ge0$, so it has infinite Tor
amplitude. The complex $[A\xrightarrow{\ell}A]$ is a bounded complex of finite free modules, hence of finite
Tor amplitude, but its cohomology is $\mathbf F_\ell$ in both degrees.
