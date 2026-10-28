+++
id = "lem-weil-pbc-truncation-step-ses"
kind = "lemma"
title = "The step tau_{<=q-1}K -> tau_{<=q}K of canonical truncations: short exact sequence and quasi-isomorphism of the cokernel to H^q(K)[-q]"
lean = ["CochainComplex.exists_upperTruncationStepSES"]
order = 2129
uses = ["def-weil-abstract-derived-category"]
tags = ["stacks-08J5"]
+++
Let $\mathcal A$ be an abelian category and $K$ a cochain complex of $\mathcal A$ with differentials $d^r:K^r\to K^{r+1}$ and cohomology $H^r(K)=\Ker d^r/\Im d^{r-1}$ [def-weil-abstract-derived-category]. For $q\in\mathbf Z$ let $\tau_{\leq q}K$ be the subcomplex $\cdots\to K^{q-2}\to K^{q-1}\to\Ker(d^q)\to0\to\cdots$ of $K$ (so $(\tau_{\leq q}K)^r=K^r$ for $r<q$, $=\Ker d^q$ for $r=q$, $=0$ for $r>q$), and let $H^q(K)[-q ]$ be the complex with $H^q(K)$ in degree $q$ and $0$ elsewhere. Then:
(a) $\tau_{\leq q-1}K$ is a subcomplex of $\tau_{\leq q}K$; the inclusion $i_q$ is a monomorphism of complexes, and its cokernel $M_q(K)=\tau_{\leq q}K/\tau_{\leq q-1}K$ (formed degreewise) is the complex with $M_q(K)^{q-1}=K^{q-1}/\Ker d^{q-1}$, $M_q(K)^q=\Ker d^q$, differential $M_q(K)^{q-1}\to M_q(K)^q$ induced by $d^{q-1}$, and $0$ in all other degrees; thus $0\to\tau_{\leq q-1}K\xrightarrow{i_q}\tau_{\leq q}K\xrightarrow{p_q}M_q(K)\to0$ is a short exact sequence of complexes ($p_q$ the quotient map).
(b) The morphism of complexes $j_q:\tau_{\leq q}K\to H^q(K)[-q ]$ that is the projection $\Ker d^q\to H^q(K)$ in degree $q$ and $0$ elsewhere factors uniquely as $j_q=\bar j_q\circ p_q$, and $\bar j_q:M_q(K)\to H^q(K)[-q ]$ (the projection $\Ker d^q\to H^q(K)$ in degree $q$) is a quasi-isomorphism: $H^{q-1}(M_q(K))=0$ because $K^{q-1}/\Ker d^{q-1}\to\Ker d^q$ is a monomorphism, and $H^q(\bar j_q)$ is the identity of $\Ker d^q/\Im d^{q-1}=H^q(K)$.
(c) Everything is natural in $K$: a morphism of complexes $f:K\to L$ restricts to morphisms $\tau_{\leq q}f$, $\tau_{\leq q-1}f$, induces $M_q(f)$, and $(\tau_{\leq q-1}f,\tau_{\leq q}f,M_q(f))$ is a morphism of short exact sequences with $H^q(f)[-q ]\circ\bar j_q=\bar j_q\circ M_q(f)$.
