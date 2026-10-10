+++
id = "lem-trf-weil-shriek-iterates"
kind = "lemma"
title = "Iterates of the Weil $!$-pushforward"
order = 2365
uses = ["d-relative-frob", "def-exchange-projection", "def-trf-frobenius-coefficient-morphism", "def-trf-weil-shriek-pushforward", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "fix-lem-exchanges", "prop-functor-package"]
+++
In the setting of [def-trf-weil-shriek-pushforward], let
$K\in D^b_{ctf}(X,A)$ and $m,n\geq1$.

1. *Base-change composition.* After the pullback composition
identifications $L\Phi^{(m+n)*}\simeq L\Phi^{m*}L\Phi^{n*}$ on $X$
and on $Y$,
$$
\theta_{f,m+n,K}=\theta_{f,m,L\Phi_X^{n*}K}\circ
L\Phi_Y^{m*}\theta_{f,n,K}:
L\Phi_Y^{(m+n)*}Rf_!K\longrightarrow Rf_!L\Phi_X^{(m+n)*}K .
$$
1. *Iterates.* Let $u:L\Phi_X^*K\to K$ be a Frobenius coefficient
morphism, with iterates $u_m$ of
[def-trf-frobenius-coefficient-morphism], and let
$\psi=Rf_!u\circ\theta_{f,1}$ be the Weil $!$-pushforward. Then the
iterates $\psi_m$ of the Frobenius coefficient morphism $\psi$ on
$Rf_!K$ satisfy
$$
\psi_m=Rf_!u_m\circ\theta_{f,m}\qquad(m\geq1).
$$

Neither statement uses invertibility of $u$.
