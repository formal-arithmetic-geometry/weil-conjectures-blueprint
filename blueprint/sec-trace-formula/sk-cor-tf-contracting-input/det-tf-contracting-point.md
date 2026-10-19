+++
id = "det-tf-contracting-point"
kind = "lemma"
title = "The restricted correspondence at a point"
uses = ["det-tf-contracting-restricted-morphism", "lem-trf-local-term-point", "def-trf-graph-correspondence"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be a correspondence of separated finite-type schemes over an
algebraically closed field $k$, let $y\in X(k)$, and suppose that $c_1^{-1}(y)$ is a single
reduced point $z$ with $c_2(z)=y$ and that $\beta=\{z\}$ is a reduced open-and-closed
component of $F_c$. Let $K\in\Dctf(X,A)$, $u:c_2^*K\to c_1^!K$, and let
$c_Z$ and $u_Z$ be the restricted correspondence and morphism of
[det-tf-contracting-restricted-morphism] for $Z=\{y\}$. Then $C_Z=\{z\}$, $c_Z$ is the
identity correspondence of the point $\operatorname{Spec}k$, $F_{c_Z}\times_{F_c}\beta=\beta$,
and $u_Z$ is an endomorphism of the stalk $K_{\bar y}$, whose local term
([lem-trf-local-term-point]) is $\operatorname{tr}_A(u_Z\mid K_{\bar y})$. If
$c_1=\operatorname{id}_X$, as for the graph correspondence $c=(\operatorname{id}_X,h)$
([def-trf-graph-correspondence]), then $u_Z=u_{\bar y}$ is the stalk map of $u$ at $y$.
