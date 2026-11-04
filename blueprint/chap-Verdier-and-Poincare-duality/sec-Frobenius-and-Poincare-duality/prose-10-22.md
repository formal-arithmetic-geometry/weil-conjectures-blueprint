+++
id = "prose-10-22"
kind = "hidden"
title = "Frobenius and Poincaré duality (1)"
order = 874
+++
Let $X_0$ be smooth of pure dimension $d$ and let $K$ be locally perfect, so
that $\mathbb D_XK\simeq K^\vee(d)[2d]$. Cup product pairs $H^i_c(X,K)$
with $H^{2d-i}(X,K^\vee)$ and takes values in $H^{2d}_c(X,\Lambda)$. To
use this pairing for the Weil conjectures we need to know how $F$ acts
on both sides. The target is not the trivial Weil complex but
$\Lambda(-d)$, as for $\mathbf P^1$ above. If we forgot the twist, we
would predict the relation $\alpha\leftrightarrow1/\alpha$ between
eigenvalues in complementary degrees instead of
$\alpha\leftrightarrow q^d/\alpha$.

We built Poincaré duality from the purity isomorphism $\gamma_f$ and the
trace map. It therefore suffices to check that these two maps commute with
pullback along Frobenius
(Proposition [proposition-purity-trace-commute-frobenius]). This
statement about natural transformations is transport of structure, except
for the identification of Tate twists. There we use that pullback along
$\operatorname{Fr}_T$ respects Kummer classes. The compatibility
of the duality pairing with Weil structures then follows formally
(Theorem [theorem-poincare-duality-frobenius]).

Let $f$ be obtained from a smooth morphism $f_0:X_0\to Y_0$ over
$k_0=\mathbf F_q$ by extension to $k$, let $\operatorname{Fr}_X$,
$\operatorname{Fr}_Y$ be the geometric Frobenius maps above, and let
$\gamma_f$ be the isomorphism of (9.2).
