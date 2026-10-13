+++
id = "pur9-cs-input-phi-local"
kind = "remark"
title = "Étale-local compatibility of the tensor comparison"
order = 2337
tags = ["latex:bpinput"]
uses = ["pur713-lem-monoidal-pullback", "pur9-cs-def-phi", "pur9-input-ambient-composition", "pur9-input-etale-normalization", "pur9-lem-upper-shriek-composition"]
+++
Assume Inputs [pur9-input-ambient-composition] and [pur9-input-etale-normalization]. Let $f:X\to Y$ and $f':X'\to Y'$ be smooth and separated, and let $u:X'\to X$, $w:Y'\to Y$ be étale with $fu=wf'$. For $K\in D^b_{ctf}(Y_{\Proet},\mathcal O_E/\varpi^n)$ let

$$
\begin{aligned}
\rho_K:Lu^*_{\mathcal O_E/\varpi^n}Rf^!_{\mathcal O_E/\varpi^n}K&\xrightarrow{\epsilon_u^{-1}}Ru^!_{\mathcal O_E/\varpi^n}Rf^!_{\mathcal O_E/\varpi^n}K\xrightarrow{c_{f,u}^{-1}}R(fu)^!_{\mathcal O_E/\varpi^n}K=R(wf')^!_{\mathcal O_E/\varpi^n}K\\
&\xrightarrow{c_{w,f'}}Rf'^!_{\mathcal O_E/\varpi^n}Rw^!_{\mathcal O_E/\varpi^n}K\xrightarrow{Rf'^!_{\mathcal O_E/\varpi^n}\epsilon_w}Rf'^!_{\mathcal O_E/\varpi^n}Lw^*_{\mathcal O_E/\varpi^n}K,
\end{aligned}
$$

in $D(X'_{\Proet},\mathcal O_E/\varpi^n)$, with $\epsilon$ of Input [pur9-input-etale-normalization] and $c$ of Lemma [pur9-lem-upper-shriek-composition]; let

$$
\rho'_K:Lu^*_{\mathcal O_E/\varpi^n}(Lf^*_{\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}\omega_f)\to Lf'^*_{\mathcal O_E/\varpi^n}Lw^*_{\mathcal O_E/\varpi^n}K\otimes^L_{\mathcal O_E/\varpi^n}\omega_{f'}
$$

be the monoidal comparison of Lemma [pur713-lem-monoidal-pullback], followed by the composition comparisons $\mu$ of Lemma “The finite-coefficient inverse-image composition comparison is invertible” (`pur713-lem-pull-composition`) for $fu=wf'$ on the first factor and by $\rho_{(\mathcal O_E/\varpi^n)_Y}$ together with the unit comparison $Lw^*_{\mathcal O_E/\varpi^n}(\mathcal O_E/\varpi^n)_Y\cong(\mathcal O_E/\varpi^n)_{Y'}$ on the second. Then $\rho_K\circ Lu^*_{\mathcal O_E/\varpi^n}(\varphi_{f,K})=\varphi_{f',Lw^*_{\mathcal O_E/\varpi^n}K}\circ\rho'_K$, with $\varphi$ of Definition [pur9-cs-def-phi]. *Status:* this is a compatibility of the projection maps with the étale normalization of Input [pur9-input-etale-normalization]; it is not established here.
