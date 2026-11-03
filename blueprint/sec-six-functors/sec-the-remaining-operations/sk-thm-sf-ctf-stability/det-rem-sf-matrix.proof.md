+++
kind = "proof"
of    = "det-rem-sf-matrix"
uses = ["sk-prop-sf-rf-shriek-preservation", "sk-cor-sf-direct-image-ctf", "sk-prop-ctf-finite-proper"]
+++
Pullback, tensor product and extension by zero preserve bounded constructible
flat models. If $p$ is proper, proper finiteness gives constructibility of
$Rp_*K$, and the scalar projection formula together with the finite
cohomological dimension of $p$ gives its finite Tor amplitude as in
[sk-cor-sf-direct-image-ctf] (see [sk-prop-ctf-finite-proper]). For a
compactification $f=pj$ this proves the assertion for $Rf_!=Rp_*j_!$, and
$Rf_*=Rp_*Rj_*$ gives it for $Rf_*$, using [sk-cor-sf-direct-image-ctf] for
$Rj_*$. The case of $f^!$ is [sk-prop-sf-rf-shriek-preservation].

For internal Hom we argue by dévissage along the strata on which the first
argument is perfect. Choose a finite stratification on which a bounded
constructible flat model of the first argument is locally a finite complex of
finite projective modules. On such a stratum a complex $P$ is dualizable, so

$$
R\mathcal Hom_A(P,L)=P^\vee\otimes_A^{\mathbf L}L
$$

lies in $\Dctf$ whenever $L$ does. To pass from the strata to $X$, use open and
closed localization triangles in the first argument together with the
identities

$$
\begin{aligned}
R\mathcal Hom_A(j_!P,L)&\simeq Rj_*R\mathcal Hom_A(P,j^*L),\\
R\mathcal Hom_A(i_*P,L)&\simeq i_*R\mathcal Hom_A(P,i^!L)
\end{aligned}
$$

in $D(X_{\mathrm{proét}},A)$, for an open immersion $j$ and a closed immersion
$i$. They follow from tensor-Hom adjunction and the adjunctions for $j_!$ and
$i_*$, and the preceding results keep both right sides in $\Dctf$. Induction
on the number of strata gives the result. (Compare [det-thm-sf-hom-ctf] for the
explicit internal-Hom bounds, [sk-thm-sf-ctf-stability] and
[det-prop-sf-finiteness] for the remaining cells, and
[det-prop-sf-biduality-general] for the dualizing functor
$\mathbb D_X=R\mathcal Hom_A(-,\omega_X)$, which preserves $\Dctf$ by the
$f^!$ and $R\mathcal Hom_A$ cases.)
