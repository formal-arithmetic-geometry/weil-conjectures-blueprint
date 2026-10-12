+++
id = "lem-trf-weil-shriek-operator-fibres"
kind = "lemma"
title = "Global operator and fibres of the Weil $!$-pushforward"
order = 2704
uses = ["d-relative-frob", "def-exchange-projection", "def-trf-frobenius-coefficient-morphism", "def-trf-scheme-frobenius", "def-trf-weil-shriek-pushforward", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "fix-lem-exchanges", "i-relative-frob", "lem-trf-adjoint-mate", "lem-trf-weil-shriek-iterates", "prop-functor-package", "prop-trf-graph-operator"]
+++
In the setting of [def-trf-weil-shriek-pushforward], let
$K\in D^b_{ctf}(X,A)$, let $u:L\Phi_X^*K\to K$ be a Frobenius
coefficient morphism of [def-trf-frobenius-coefficient-morphism] (no
invertibility assumed), and let $(L,\psi)=(Rf_!K,Rf_!u\circ\theta_{f,1})$
be its Weil $!$-pushforward, with iterates
$\psi_m=Rf_!u_m\circ\theta_{f,m}$ ([lem-trf-weil-shriek-iterates]).

1. *Global operators.* Let
$c_f:R\Gamma_c(Y,Rf_!K)\xrightarrow{\sim}R\Gamma_c(X,K)$ be the
composition isomorphism for $a_Yf=a_X$ ([prop-functor-package],
clause (3)). For every $m\geq1$ the global operators of
[def-trf-frobenius-coefficient-morphism] satisfy
$$
c_f\circ F_{c,m}(\psi)=F_{c,m}(u)\circ c_f .
$$
1. *Fibres.* Let $m\geq1$, $y\in Y_0(\mathbf F_{q^m})$, and let
$\bar y:\operatorname{Spec}k\to Y$ be the geometric point over $y$, so
that $\Phi_Y^m\bar y=\bar y$. Put $X_{\bar y}=X\times_{f,Y,\bar y}\operatorname{Spec}k$,
with $i_{\bar y}:X_{\bar y}\to X$, and $K|_{\bar y}=Li_{\bar y}^*K$.
Then $X_{\bar y}=X_{0,y}\times_{\mathbf F_{q^m}}k$ for the separated
finite-type $\mathbf F_{q^m}$-scheme $X_{0,y}=X_0\times_{Y_0,y}\operatorname{Spec}\mathbf F_{q^m}$,
and for the finite-field datum with $q$ replaced by $q^m$
([def-weil-finite-field-fiber]) the $q^m$-power scheme Frobenius of
$X_{0,y}$ is the restriction $\Phi_{X_{\bar y}}$ of $\Phi_X^m$. The
composite
$$
u_m|_{\bar y}:L\Phi_{X_{\bar y}}^*K|_{\bar y}\xrightarrow{\ \sim\ }
Li_{\bar y}^*L\Phi_X^{m*}K\xrightarrow{\ Li_{\bar y}^*u_m\ }K|_{\bar y}
$$
is a Frobenius coefficient morphism for this datum, and the proper
base-change isomorphism
$\beta_{\bar y}:L_{\bar y}=\bar y^*Rf_!K\xrightarrow{\sim}R\Gamma_c(X_{\bar y},K|_{\bar y})$
([prop-functor-package], clause (4)) satisfies
$$
\beta_{\bar y}\circ\psi_{m,\bar y}=F_{c,1}\bigl(u_m|_{\bar y}\bigr)\circ\beta_{\bar y},
$$
where $\psi_{m,\bar y}:L_{\bar y}\cong(L\Phi_Y^{m*}L)_{\bar y}\to L_{\bar y}$
is the stalk map of $\psi_m$ at the fixed point $\bar y$ and $F_{c,1}$ is
the degree-one global operator over $\mathbf F_{q^m}$.
1. *Points and stalks.* $X_0(\mathbf F_{q^m})$ is the disjoint union of
the sets $X_{0,y}(\mathbf F_{q^m})$ over $y\in Y_0(\mathbf F_{q^m})$, and
for $x\in X_{0,y}(\mathbf F_{q^m})$ with geometric point $\bar x$ the
stalk map of $u_m|_{\bar y}$ at $\bar x$ is the stalk map $u_{m,\bar x}$.

Invertibility of $u$ is used nowhere.
