+++
kind = "proof"
of = "det-tf-fixed-deformation-immersion"
uses = ["det-tf-fixed-ideal-nilpotent", "det-tf-cone-leg-lifts"]
+++
Since $H^r$ is the image of $J^r$ in $\mathcal O_F$ for every $r$, the restriction map
induces a surjection of deformation algebras

$$
 \mathcal O_{C_T}[J/t]\twoheadrightarrow\mathcal O_{F_T}[H/t],
$$

hence a closed immersion $\mathcal D_{a^{-1}(Z)}F\hookrightarrow\mathcal D_EC$. Its composites
with $\widetilde c_1$ and $\widetilde c_2$ are the lifts of $a_T=c_{1}|_F=c_2|_F$ given by
[det-tf-cone-leg-lifts], and these lifts are unique, so the two composites are equal and the
immersion factors through the equalizer $\widetilde F$. By [det-tf-fixed-ideal-nilpotent],
$H$ is nilpotent, so each generator $h/t$ with $h\in H$ is nilpotent, and the reduction of
$\mathcal O_{F_T}[H/t]$ is that of $\mathcal O_{F_T}$. Thus the reduction of
$\mathcal D_{a^{-1}(Z)}F$ is $(F_T)_{\mathrm{red}}$.
