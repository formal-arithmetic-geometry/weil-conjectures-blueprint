+++
kind = "proof"
of = "det-pe-replete-definition"
+++
The data are well defined. The displayed presheaf is a sheaf: limits of sheaves commute
with the equalizer diagrams expressing the sheaf condition, so the sectionwise limit of
sheaves satisfies the sheaf condition, and it has the universal property of the limit in
$\mathcal T$ because it has it in presheaves and $\mathcal T$ is a full subcategory. The
categorical epimorphisms of $\mathcal T$ are exactly the locally surjective maps: a
locally surjective map is an epimorphism by the sheaf condition (two maps out of $G$ that
agree after composing with $\varphi$ agree on every $y$ locally, hence globally);
conversely, if $\varphi$ is an epimorphism, its image sheaf $\operatorname{im}\varphi$ (the
sheaf of locally-in-the-image sections) is a subobject through which $\varphi$ factors,
and the two maps $G\rightrightarrows G\amalg_{\operatorname{im}\varphi}G$ agree after
$\varphi$, hence are equal; since in a topos every monomorphism is the equalizer of its
cokernel pair, this forces $\operatorname{im}\varphi=G$.
