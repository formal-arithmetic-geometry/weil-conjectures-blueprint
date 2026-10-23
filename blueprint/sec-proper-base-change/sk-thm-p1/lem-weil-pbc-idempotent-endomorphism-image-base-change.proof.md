+++
kind = "proof"
of = "lem-weil-pbc-idempotent-endomorphism-image-base-change"
+++
(i) Since $p^2=p$, $\ker p=\operatorname{Im}(1-p)$: if $p(v)=0$ then $v=(1-p)(v)$, and $p(1-p)=p-p^2=0$. Every $v$ is $p(v)+(1-p)(v)$, and if $v\in\operatorname{Im}(p)\cap\ker p$ then $v=p(v)=0$; so $R^{\oplus n}=\operatorname{Im}(p)\oplus\operatorname{Im}(1-p)$. $\operatorname{Im}(p)$ is finitely generated as the image of a finite module. The corestriction $r:R^{\oplus n}\to\operatorname{Im}(p)$ of $p$ is a retraction of the inclusion $i:\operatorname{Im}(p)\to R^{\oplus n}$ (as $p$ is the identity on its image), so $\operatorname{Im}(p)$ is a direct summand of a finite free module, hence projective.

(ii) Let $E:R^{\oplus n}\otimes_RS\xrightarrow{\sim}S^{\oplus n}$ be the canonical $S$-linear isomorphism, $x\otimes s\mapsto s\cdot\rho(x)$. Base-change $i$ and $r$ to $i_S$ and $r_S$; the identity $r_S\circ i_S=\mathrm{id}$ holds on pure tensors, hence everywhere. Set $f=E\circ i_S:\operatorname{Im}(p)\otimes_RS\to S^{\oplus n}$ and $g=r_S\circ E^{-1}$; then $g\circ f=\mathrm{id}$. On pure tensors $f(v\otimes s)=s\cdot\rho(v)$, which is the map of the statement.

On pure tensors $E(i_S(r_S(x\otimes s)))=s\cdot\rho(Xx)=s\cdot\rho(X)\rho(x)=p_S(E(x\otimes s))$, since applying $\rho$ to coordinates commutes with matrix-vector multiplication. Therefore $f\circ g=p_S$. From $g\circ f=\mathrm{id}$ and $f\circ g=p_S$ we get $p_S^2=f\circ(g\circ f)\circ g=p_S$, $f$ is injective, and $\operatorname{Im}(f)=\operatorname{Im}(p_S)$ (as $g$ is surjective). Thus $f$ is an isomorphism $\operatorname{Im}(p)\otimes_RS\cong\operatorname{Im}(p_S)$, compatible with the inclusions into $S^{\oplus n}$.
