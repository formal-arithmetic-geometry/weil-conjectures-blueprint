+++
kind  = "proof"
of    = "sk-input-weights"
+++
The constant sheaf has weight zero, since its local Frobenius is the
identity ([sk-d-real-weights]). Apply [sk-prop-smooth-proper-purity] to the
structure map. The embedding $\iota$ was arbitrary in
[sk-cor-dl-general-complex] and in the duality argument, so we may apply them
to each embedding separately.

For the complement: [sk-cor-dl-general-complex] applied to the structure
morphism and the constant sheaf, which is mixed of weights at most $0$,
shows that $H_c^{i}(X,\Qlb)$ is $\iota$-mixed of weights at most $i$; as
$X_0$ is proper, $Ra_{X_0!}\to Ra_{X_0*}$ is an isomorphism of Weil data
([sk-prop-sf-comp-proper]), which gives the Frobenius-equivariant comparison.
Over $\Qlb$ one has $\det(1-TF\mid H^i(X,\Ql))=\prod_\beta(1-\beta T)$, the
product over the eigenvalues $\beta$ of $F$ counted with multiplicity, so the
reciprocal roots are exactly these eigenvalues, and the main assertion
applies to them.
