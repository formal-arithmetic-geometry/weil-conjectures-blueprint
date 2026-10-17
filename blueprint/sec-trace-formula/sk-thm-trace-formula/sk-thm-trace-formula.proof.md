+++
kind = "proof"
of = "sk-thm-trace-formula"
uses = ["sk-thm-tf-coefficient-morphism-formula", "sk-lem-tf-frobenius-convention", "sk-lem-tf-fixed-points"]
+++
Apply [sk-thm-tf-coefficient-morphism-formula] to
$\psi=\phi\kappa_1$ and use
[sk-lem-tf-frobenius-convention], which identifies
$T_{c_m}(\psi_m)$ with $\operatorname{Frob}_{X,K}^m$ and, at each fixed
point, $\psi_{m,\bar y}$ with $\operatorname{Frob}_{y,m}$.

*Complement.* The fixed points of $\Phi_X^m$ are the points of
$X_0(\mathbf F_{q^m})$ by [sk-lem-tf-fixed-points]. The identity is the case of
an invertible $\psi$ in [sk-thm-tf-coefficient-morphism-formula], which
assumes no invertibility.
