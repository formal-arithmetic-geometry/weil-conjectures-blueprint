+++
kind = "proof"
of = "pur9-cs-lem-invertible"
uses = ["pur7710-lem-constructible-equivalence", "pur9-def-tate-twist", "pur9-input-etale-normalization", "pur9-input-preservation", "pur9-lem-open-immersion-upper-shriek", "pur9-lem-upper-shriek-composition", "pur9-lem-vector-bundle-purity"]
+++
By Input [pur9-input-preservation] and Lemma [pur7710-lem-constructible-equivalence], $\omega_f\cong L\nu^*_{X,\mathcal O_E/\varpi^n}G$ for some $G\in D^b_c(X_{\Et},\mathcal O_E/\varpi^n)$. With the charts of the proof of Lemma [pur9-cs-lem-tensor-formula], Lemma [pur9-lem-upper-shriek-composition], Input [pur9-input-etale-normalization] and Lemma [pur9-lem-open-immersion-upper-shriek] give

$$
\begin{aligned}
Lu^*_{x,\mathcal O_E/\varpi^n}\omega_f&\cong Ru^!_{x,\mathcal O_E/\varpi^n}Rf^!_{\mathcal O_E/\varpi^n}(\mathcal O_E/\varpi^n)_Y\cong R(p_dv_x)^!_{\mathcal O_E/\varpi^n}Rw^!_{x,\mathcal O_E/\varpi^n}(\mathcal O_E/\varpi^n)_Y\\
&\cong Rv^!_{x,\mathcal O_E/\varpi^n}Rp^!_{d,\mathcal O_E/\varpi^n}(\mathcal O_E/\varpi^n)_{Y_x}\cong Lv^*_{x,\mathcal O_E/\varpi^n}\omega_{p_d},
\end{aligned}
$$

and $\omega_{p_d}\cong(\mathcal O_E/\varpi^n)_{\Aaf^d_{Y_x}}(d)[2d]$ by Lemma [pur9-lem-vector-bundle-purity]. By Definition [pur9-def-tate-twist] this twist is presented by an étale complex concentrated in degree $-2d$ whose cohomology sheaf is lisse of rank one; so is its inverse image along $v_x$. By Definition “Inverse image across the two sites” (`pur7710-def-site-pullback-comparison`, see [sk-prop-sf-comp-coherence]) and full faithfulness (Lemma “Full faithfulness of the finite-coefficient site inverse image” (`pur7710-lem-site-fully-faithful`, see [sk-prop-sf-comp-coherence])), the displayed isomorphism lifts to an isomorphism of étale presentations on $(X_x)_{\Et}$. Hence, by Lemma “Stalks of étale inverse image” (`pur456-pbc-pullback-stalk`, see [sk-thm-sf-comp-composition]), the stalks of $\mathcal H^r(G)$ vanish for $r\neq-2d$ at all geometric points of $X$, so $\mathcal H^r(G)=0$ for $r\neq-2d$, and $\mathcal L_f:=\mathcal H^{-2d}(G)$ is lisse of rank one, the open sets $X_x$ forming the trivializing covering. A complex with a single nonzero cohomology sheaf is isomorphic to that sheaf shifted, so $G\cong\mathcal L_f[2d]$, and hence $\omega_f\cong L\nu^*_{X,\mathcal O_E/\varpi^n}(\mathcal L_f)[2d]$.
