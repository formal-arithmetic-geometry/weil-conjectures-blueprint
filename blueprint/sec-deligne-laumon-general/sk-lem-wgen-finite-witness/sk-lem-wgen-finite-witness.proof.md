+++
kind  = "proof"
of    = "sk-lem-wgen-finite-witness"
+++
We first recall why an algebra $A\subset\operatorname{End}(V)$
acting irreducibly on a vector space over an algebraically closed
field equals $\operatorname{End}(V)$ (Burnside's theorem). For
linearly independent $v_1,\ldots,v_r$, consider the map
$a\mapsto(av_1,\ldots,av_r)$. By induction its image projects onto
$V^{r-1}$, and the intersection of the image with the last copy of
$V$ is either $V$ or zero. In the second case the image is the graph
of an $A$-linear map $V^{r-1}\to V$, which by Schur's lemma has the
form $(x_i)\mapsto\sum c_ix_i$; evaluating at $1\in A$ contradicts the
independence of the $v_i$. Thus the map is onto, and taking for the
$v_i$ a basis proves the assertion about $A$.

The compact group $\rho(\Pi)$ stabilizes a lattice $L$. Indeed, all
translates of an initial lattice $L_0$ lie in $\pi_E^{-a}L_0$ for one
$a$, and their $\mathcal O_E$-span is a finitely generated
torsion-free module containing $L_0$. By absolute irreducibility and
the preceding argument, there are elements $g_1,\ldots,g_{n^2}$ whose
matrices span $\operatorname{End}_E(V)$. In a basis of $L$, the
determinant $\Delta$ of their matrices, written as column vectors, is
nonzero and integral. Choose $N>v_{\pi_E}(\Delta)$. Matrices
congruent to these modulo $\pi_E^N$ still have nonzero determinant in
the same sense. Therefore every subgroup as in the statement spans the
whole matrix algebra, also after any field extension, and so it acts
absolutely irreducibly. The image of $\Pi$ on $L/\pi_E^NL$ is finite
by continuity.
