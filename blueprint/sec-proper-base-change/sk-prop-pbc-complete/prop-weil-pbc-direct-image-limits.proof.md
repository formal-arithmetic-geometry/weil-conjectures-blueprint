+++
kind  = "proof"
of    = "prop-weil-pbc-direct-image-limits"
uses = ["det-pbc-complete-derived-completion"]
+++
We use the characterization of derived completeness by right orthogonality in
[det-pbc-complete-derived-completion]. Let $Z\in D(Y)$ be an object on which
$\varpi$ acts invertibly and $u:Z\to Rf_*K$ a morphism. Under the adjunction
$f^*\dashv Rf_*$ between the derived inverse and direct images, $u$ corresponds
to $u^\flat:f^*Z\to K$. The functor $f^*$ is $R$-linear, so $\varpi$ acts
invertibly on $f^*Z$, and $u^\flat=0$ because $K$ is derived complete. Hence
$u=0$, and $Rf_*K$ is derived complete.
