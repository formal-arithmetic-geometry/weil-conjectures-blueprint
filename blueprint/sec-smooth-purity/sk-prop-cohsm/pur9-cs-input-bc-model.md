+++
id = "pur9-cs-input-bc-model"
kind = "remark"
title = "Base change on the affine-space model"
order = 2346
tags = ["latex:bpinput"]
uses = ["pur9-cs-def-bc", "pur9-def-purity-comparison", "pur9-def-tate-twist"]
+++
For $p_d:\Aaf^d_Y\to Y$ and $v:Y'\to Y$, with base change $p'_d:\Aaf^d_{Y'}\to Y'$ and projection $u:\Aaf^d_{Y'}\to\Aaf^d_Y$, the map $b_{v,(\mathcal O_E/\varpi^n)_Y}$ of Definition [pur9-cs-def-bc], followed by $Rp'^!_{d,\mathcal O_E/\varpi^n}$ of the unit comparison $Lv^*_{\mathcal O_E/\varpi^n}(\mathcal O_E/\varpi^n)_Y\cong(\mathcal O_E/\varpi^n)_{Y'}$, satisfies

$$
\gamma_{p'_d,(\mathcal O_E/\varpi^n)_{Y'}}^{-1}\circ b_{v,(\mathcal O_E/\varpi^n)_Y}\circ Lu^*_{\mathcal O_E/\varpi^n}(\gamma_{p_d,(\mathcal O_E/\varpi^n)_Y})=\tau_u,
$$

where $\gamma$ is Definition [pur9-def-purity-comparison] and $\tau_u:Lu^*_{\mathcal O_E/\varpi^n}(\mathcal O_E/\varpi^n)_{\Aaf^d_Y}(d)[2d]\cong(\mathcal O_E/\varpi^n)_{\Aaf^d_{Y'}}(d)[2d]$ is the inverse-image isomorphism of Definition [pur9-def-tate-twist]. *Status:* this is the base-change compatibility of the model purity comparison of -prop-anZZ, stated there; it is recorded here as the precise form used.
