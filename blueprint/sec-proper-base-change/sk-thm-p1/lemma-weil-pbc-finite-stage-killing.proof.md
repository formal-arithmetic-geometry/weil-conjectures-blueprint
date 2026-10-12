+++
kind  = "proof"
of    = "lemma-weil-pbc-finite-stage-killing"
+++
Represent the chosen cochain and its null-homotopy on the limit by finitely
many sections. Each section and each equality occurs at some index because
the system is filtered and the etale site is quasi-compact and quasi-separated.
Choose one index dominating those finitely many indices. The descended
cochain and the descended null-homotopy satisfy the coboundary equation at a
further finite index; replacing by that index gives $\lambda_0$.

The $T_\lambda\to T$ are finite, hence affine, so $(T_\lambda)$ is a
cofiltered inverse system of quasi-compact quasi-separated schemes with affine
transition maps (finite morphisms being affine); base changing along the
closed immersion $T_0\hookrightarrow T$ of the affine henselian pair, the
system $((T_\lambda)_0)$ is of the same kind, with limit $X_0=X\times_TT_0$,
and the pullbacks of the torsion sheaf $F_0$ form a compatible system. By the
continuity of etale cohomology along such limits,

$$
 \varinjlim_\lambda H^q((T_\lambda)_0,F_0|)
 \xrightarrow{\sim}H^q(X_0,F_0|),
$$

and the hypothesis that $c$ vanishes after pullback to the integral strictly
local cover $X$ says exactly that the element $(c|_{(T_\lambda)_0})$ maps to
zero in this colimit; an element of a filtered colimit that maps to zero is
already zero, so $c|_{(T_{\lambda_0})_0}=0$ for some $T_{\lambda_0}$, as
asserted.
