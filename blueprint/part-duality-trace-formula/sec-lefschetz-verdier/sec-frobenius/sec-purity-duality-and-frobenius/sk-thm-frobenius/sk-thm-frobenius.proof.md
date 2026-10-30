+++
kind = "proof"
of = "sk-thm-frobenius"
uses = ["sk-thm-derived-duality", "sk-prop-prop-sp-frobenius-purity"]
+++
Cup product with mixed supports and evaluation are natural for pullback
by Frobenius, and the isomorphism $\gamma_{a_X}$ and the trace map are equivariant
by Proposition [sk-prop-prop-sp-frobenius-purity]. Hence their composite
$\beta_K$ is equivariant. Geometric Frobenius acts
on $\Lambda(d)$ by $q^{-d}$ and on
$\Lambda(-d)$ by $q^d$. Removing the twist, we get the
displayed similitude identity.

For field coefficients, Corollary [sk-thm-derived-duality] identifies
$H^{2d-i}(X,K^\vee)$, via the untwisted pairing, with the dual of
$H_c^i(X,K)$ tensored with $\Lambda(-d)$. Frobenius on $H_c^i(X,K)$
is invertible, because $\phi_K$ is an isomorphism. The untwisted
identity therefore shows that Frobenius on $H^{2d-i}(X,K^\vee)$ is
$q^d$ times the inverse transpose of Frobenius on $H_c^i(X,K)$.
Since a matrix and its transpose have the same characteristic
polynomial, this proves the eigenvalue statement with algebraic
multiplicities. Taking determinants of
$F_{2d-i}=q^d\,{}^t(F_i)^{-1}$ on spaces of dimension $b$ gives
$\det F_{2d-i}=q^{db}(\det F_i)^{-1}$, where $F_i$ and $F_{2d-i}$
denote $F$ on $H^i_c(X,K)$ and on $H^{2d-i}(X,K^\vee)$.
