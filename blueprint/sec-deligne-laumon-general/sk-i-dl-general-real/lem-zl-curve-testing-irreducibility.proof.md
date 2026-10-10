+++
kind  = "proof"
of    = "lem-zl-curve-testing-irreducibility"
+++
Use the geometric representations of
[def-wf-fundamental-representation], and choose finite coefficient
fields for them as allowed in [def-weil-pbc-qbar-category].
By [lem-zl-finite-matrix-irreducibility], each has a finite
reduction quotient detecting absolute irreducibility. Intersect
their open normal kernels in $\pi_1(X)$, where
$X=X_0\times\overline{\mathbf F}_q$. The resulting finite quotient
$Q$ corresponds to a connected finite etale Galois cover $T\to X$.
For $\dim X\geq2$, apply
[lem-zl-bertini-finite-cover-curve]. Connectedness of the
restricted $Q$-torsor means that the image of $\pi_1(C)$ acts
transitively on $Q$, hence is all of $Q$. It surjects onto each
chosen reduction quotient. The finite matrix witnesses show that
all the restricted geometric representations remain irreducible.
The curve and inclusion descend to a finite constant extension;
the restrictions inherit their Weil structures over that field.
For dimension one take $C=X$, with its given finite-field model.
