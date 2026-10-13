+++
id = "pur9-cs-input-bc-composition"
kind = "remark"
title = "Compatibility of the base-change maps with composite Cartesian squares"
order = 2344
tags = ["latex:bpinput"]
uses = ["pur713-input-comparison", "pur9-cs-def-bc", "pur9-cs-input-constructible-closure"]
+++
In the situation of Definition [pur9-cs-def-bc], let $v_2:Y''\to Y'$ be a further morphism, $X''=X'\times_{Y'}Y''$ with projections $f'':X''\to Y''$ and $u_2:X''\to X'$, so that the outer square, formed with $v_1:=v$, $v_1v_2$, $u_1:=u$, $u_1u_2$, is Cartesian with $X''\cong X\times_YY''$. For $K\in D^b_{ctf}(Y_{\Proet},\mathcal O_E/\varpi^n)$,

$$
b_{v_1v_2,K}\circ\mu_{u_1,u_2,\mathcal O_E/\varpi^n,Rf^!_{\mathcal O_E/\varpi^n}K}
=Rf''^!_{\mathcal O_E/\varpi^n}(\mu_{v_1,v_2,\mathcal O_E/\varpi^n,K})\circ b_{v_2,Lv^*_{1,\mathcal O_E/\varpi^n}K}\circ Lu^*_{2,\mathcal O_E/\varpi^n}(b_{v_1,K})
$$

as morphisms $Lu^*_{2,\mathcal O_E/\varpi^n}Lu^*_{1,\mathcal O_E/\varpi^n}Rf^!_{\mathcal O_E/\varpi^n}K\to Rf''^!_{\mathcal O_E/\varpi^n}L(v_1v_2)^*_{\mathcal O_E/\varpi^n}K$ in $D(X''_{\Proet},\mathcal O_E/\varpi^n)$, where $\mu$ are the composition comparisons of Definition “Composition comparison for finite-coefficient derived inverse image” (`pur713-def-pull-composition`), invertible by Lemma “The finite-coefficient inverse-image composition comparison is invertible” (`pur713-lem-pull-composition`), and $b_{v_2,Lv^*_{1,\mathcal O_E/\varpi^n}K}$ is formed for $f'$ (note $Lv^*_{1,\mathcal O_E/\varpi^n}K\in D^b_{ctf}(Y'_{\Proet},\mathcal O_E/\varpi^n)$ by Input [pur9-cs-input-constructible-closure]). For $v_2=\mathrm{id}$ the map $b_{\mathrm{id},K}$ is the identity after the identity comparisons $\iota$. *Status:* not established here; it requires the compatibility of the compact-support exchanges $\operatorname{Ex}^\circ_!$ and of the comparisons $\theta$ of Input [pur713-input-comparison] with pasting of Cartesian squares, which is not proved in this manuscript.
