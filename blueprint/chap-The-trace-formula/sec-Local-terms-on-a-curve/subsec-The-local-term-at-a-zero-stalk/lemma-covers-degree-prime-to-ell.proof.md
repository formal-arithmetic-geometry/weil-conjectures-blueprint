+++
kind = "proof"
of = "lemma-covers-degree-prime-to-ell"
order = 983
uses = ["lemma-covers-degree-prime-to-ell--1"]
+++
We take the fixed field of an $\ell$-Sylow subgroup of the monodromy, adjust
the degree by an Eisenstein extension, and descend to curves.

Let $F$ be the fraction field of the discrete valuation ring of $S$.
Then the punctured trait $S-s$ is $\operatorname{Spec}(F)$, so the
$\mathcal F_i$ are finite sets with a continuous action of
$\operatorname{Gal}(F^{\mathrm{sep}}/F)$. We choose a finite Galois extension $L/F$ over which all of them become constant, let $P$ be an $\ell$-Sylow
subgroup of $G=\operatorname{Gal}(L/F)$, and put $F_1=L^P$ and
$d_1=[F_1:F]=[G:P]$, which is prime to $\ell$.

Let $d=d_1e$ be a
multiple of $d_1$ prime to $\ell$. The normalization $S_1$ of $S$ in the
separable extension $F_1$ is finite over $S$, and it is local because it
is a domain finite over a henselian local ring. Hence $S_1$ is a strictly
henselian discrete valuation ring with residue field $k$, and it has
degree $d_1$ over $S$. If $e>1$, let $t$ be a uniformizer of $S_1$. The
Eisenstein polynomial $z^e+tz-t$ is irreducible, and its derivative
$ez^{e-1}+t$ is nonzero, also when $p\mid e$, so it is separable. Hence
$S'=S_1[z]/(z^e+tz-t)$ is a discrete valuation ring, totally ramified of
degree $e$ over $S_1$, with separable fraction field $F'$ over $F$. If
$e=1$ we put $S'=S_1$. Then $S'\to S$ is finite flat of degree $d$, with
a single point $s'$ over $s$, and $S'-s'=\operatorname{Spec}(F')\to
\operatorname{Spec}(F)$ is finite étale. The group
$\operatorname{Gal}(F^{\mathrm{sep}}/F')$ acts on the stalks of the
$\mathcal F_i$ through its image in $G$, which lies in
$\operatorname{Gal}(L/F_1)=P$ since $F_1\subset F'$.

Finally, by a limit
argument $S'\to S$ descends to a finite flat morphism $C'\to C$ onto an
étale neighbourhood $C$ of $s$, which we may take with normal source. Since $k$ is perfect, the normal curve $C'$ is smooth. Moreover, the morphism $C'\to C$ is étale over a dense open of $C$, and after shrinking $C$ around $s$
it is étale away from $s$. Since $k$ is algebraically closed,
$C'\times_CS$ is the product of the strict localizations of $C'$ at the
points over $s$. As it equals the local scheme $S'$, there is a single
point over $s$, and $S'$ is the strict localization of $C'$ there.
