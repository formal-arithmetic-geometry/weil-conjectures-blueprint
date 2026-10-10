+++
kind  = "proof"
of    = "prop-weil-pbc-levelwise-truncations"
+++
The evaluations $\operatorname{ev}_n$ are exact and jointly conservative, so
the levelwise t-structure of $D(\operatorname{Tow}_A(T))$ has the levelwise
canonical truncations of the statement, computed on the strict-tower
representatives.

*Step 1: the normalization isomorphisms of (i).* The derived tensor functor
$-\otimes^L_{P_{n+1}}P_n$ is triangulated, being the left derived functor of
$-\otimes_{P_{n+1}}P_n$ (take a K-flat resolution of $P_n$); tensoring the
truncation triangle of $K_{n+1}$,
$$
 \tau^{\le m}K_{n+1}\longrightarrow K_{n+1}
 \longrightarrow\tau^{\ge m+1}K_{n+1}\longrightarrow
 \tau^{\le m}K_{n+1}[1],
$$
with $P_n$ and using the normalization
$K_{n+1}\otimes^L_{P_{n+1}}P_n\simeq K_n$ gives the triangle
$$
 (\tau^{\le m}K_{n+1})\otimes^L_{P_{n+1}}P_n
 \longrightarrow K_n
 \longrightarrow(\tau^{\ge m+1}K_{n+1})\otimes^L_{P_{n+1}}P_n
 \longrightarrow .
$$
Künneth spectral sequence. For a complex $M$ of $P_{n+1}$-modules there is
the Künneth spectral sequence of the derived tensor
$$
 E_2^{p,q}=\operatorname{Tor}_p^{P_{n+1}}\bigl(\mathcal H^q(M),P_n\bigr)
 \Rightarrow\mathcal H^{q-p}\bigl(M\otimes^L_{P_{n+1}}P_n\bigr).
$$
For $M=\tau^{\le m}K_{n+1}$ one has $\mathcal H^q(M)=0$ for $q>m$, so all
the $E_2$-terms of total degree $>m$ vanish and the first end term of the
triangle has no cohomology above degree $m$. For $M=\tau^{\ge m+1}K_{n+1}$,
the $E_2$-terms of total degree $\le m$ are exactly the higher Tor-terms
$$
 \operatorname{Tor}_p^{P_{n+1}}\bigl(\mathcal H^q(K_{n+1}),P_n\bigr),
 \qquad q\ge m+1,\ p\ge q-m\ge1,
$$
of the cohomology sheaves of degree $\ge m+1$; by the same spectral sequence
applied to $K_{n+1}$, the Tor-compatibility condition (1) of the statement —
whose displayed morphisms are the $p=0$ edge terms in degrees $q\ge m+1$ —
is exactly the vanishing of all these higher Tor-terms (a sufficient
condition being the $\varpi$-torsion-freeness, i.e. flatness over the
discrete valuation ring $A_T$, of the cohomology sheaves $\mathcal H^i(K)$
of the ambient object for $i\ge m+1$, as in the statement; for the towers of
the form $K_n=QK\otimes^L_{A_T}(P_n)_T$ the cohomology sheaves of the models
are then flat over the respective $P_n$ by base change along $A_T\to P_n$).
Under (1) the second end term therefore has no cohomology in degrees $\le m$,
and the triangle above is a truncation triangle of $K_n$; truncation
triangles are unique (a triangle whose end terms, endowed with the displayed
maps, lie in the full subcategories of complexes with cohomology in $\le m$
and $\ge m+1$ respectively is canonically isomorphic to the canonical
truncation triangle of the middle term), so the canonical normalization
isomorphisms of (i) follow, and the cocycle is inherited from the quotient
cocycle of $K_\bullet$. When condition (1) fails, the displayed end terms of
the triangle carry the Tor-contributions of the Künneth spectral sequence in
the wrong degrees, and the composite is in general only a canonical
morphism, not an isomorphism; the counterexample after the statement shows the
failure is real.

*Step 2: the models of (ii).* The local models here are those of the
bounded constructible tower. (Under the Tor-compatibility condition (1),
which the hypotheses of (ii) ensure throughout: the cohomology sheaves of
the local models are the ones of the ambient object.) The terms of
$\tau^{\le m}L_{\alpha j}$ are $L_{\alpha j}^i$ for $i<m$, and $\ker(d^m)$
in degree $m$: after refining the pro-etale covering so that each
$U_{\alpha j}$ is connected, $A_T|_{U_{\alpha j}}$ is the constant completed
valuation ring, over which submodules of finite free modules are finite
free, so the terms are finite locally free. The support and the finite lisse
reduction cohomology of the models follow from the isomorphisms of (iii)
(the reductions of the truncated models have the same cohomology sheaves as
the reductions of $L_{\alpha j}$ in the surviving degrees, by Step 1 applied
locally). The terms of $C_{\alpha j}$ are direct sums of terms of
$L_{\alpha j}$ and of $\tau^{\le m}L_{\alpha j}$, hence finite locally free;
its support is $[m+1,d_1]$, and, being the cone of the model truncation map,
its reductions are constant by the same local computation, since
$$
 C_{\alpha j}\otimes^L_{A_T}(P_n)_T
 \cong\operatorname{Cone}\bigl(
   \tau^{\le m}K_n|_{U_{\alpha j}}\longrightarrow K_n|_{U_{\alpha j}}\bigr)
 \cong\tau^{\ge m+1}K_n|_{U_{\alpha j}}.
$$
The intertwinings with the quotient transition maps are the local forms of
the canonical isomorphisms of (i).

*Step 3: the cohomology isomorphisms and the witnesses of (iii).* The
formulas of (iii) hold by construction of the levelwise truncations of the
strict-tower representatives. Under condition (1), for $i\le m$ the triangle
of Step 1 has end terms with zero cohomology in the relevant degrees, so the
long exact cohomology sequence of the tensored truncation triangle yields
the displayed isomorphisms of (iii) directly (compatible with the
normalization maps of (i) by their canonicality); the etale-origin witnesses
[def-weil-pbc-etale-origin-witness] are transported by the exactness of the
site-comparison inverse image $\nu^*$
[def-weil-pbc-site-comparison-morphism]: for a witness
$K_n\simeq\nu^*L_n^{\mathrm{et}}$ one has
$\tau^{\le m}K_n\simeq\nu^*\tau^{\le m}L_n^{\mathrm{et}}$, and the
normalization compatibility is the naturality of $\nu^*$.
