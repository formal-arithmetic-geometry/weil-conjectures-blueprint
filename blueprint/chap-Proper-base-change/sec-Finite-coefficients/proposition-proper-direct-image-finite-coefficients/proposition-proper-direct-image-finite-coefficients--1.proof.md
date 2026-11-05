+++
kind = "proof"
of = "proposition-proper-direct-image-finite-coefficients--1"
order = 410002
uses = ["theorem-chow-s-lemma-projective-form", "theorem-proper-base-change-classical-pro"]
+++
Choose $d\geq 0$ bounding the dimensions of all geometric fibres of $p$.
Such a bound is obtained by descent to schemes of finite type over $k$
on a finite affine open cover of $Y$.

For a constructible étale sheaf $F$ of $A$-modules on $X$, each $R^qp_*F$
is constructible. Indeed, locally on $Y$ the proper morphism and the sheaf
descend to a scheme of finite type over $k$, and proper base change
[theorem-proper-base-change-classical-pro] identifies their higher direct
images after pullback. Over a scheme of finite type, constructibility follows
by Noetherian induction, using a projective modification from Chow's lemma
[theorem-chow-s-lemma-projective-form], the projective case, and the closed
complement of the open set on which the modification is an isomorphism.

Proper base change also identifies the geometric stalks of $R^qp_*F$ with
$H^q(X_{\bar y},F|_{X_{\bar y}})$. These groups vanish for $q>2d$ by the
cohomological-dimension bound on the geometric fibres. Since geometric
points detect zero sheaves and $Rp_*$ is left $t$-exact, $Rp_*F$ is
concentrated in $[0,2d]$. Thus $Rp_*$ sends every constructible sheaf in
degree zero to a bounded constructible complex. Induction along the
truncation triangles of a bounded constructible complex gives the assertion.
