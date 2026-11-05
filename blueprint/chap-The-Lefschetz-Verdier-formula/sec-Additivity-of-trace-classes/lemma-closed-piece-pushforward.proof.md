+++
kind = "proof"
of = "lemma-closed-piece-pushforward"
order = 940
uses = ["proposition-proper-direct-image-constructible-complexes", "lemma-passing-schematic-closure"]
+++
The maps $\alpha$ and $\beta$ of
Definition [definition-pushforward-correspondence] are here

$$
c_2^*Ri_*M\xrightarrow{\eta_{i'}}
Ri'_*i'^*c_2^*Ri_*M
=Ri'_*c_{2Z}^*i^*Ri_*M
\xrightarrow{Ri'_*c_{2Z}^*\varepsilon_i}Ri'_*c_{2Z}^*M
$$

and the map $Ri'_*c_{1Z}^!M\to c_1^!Ri_*M$ adjoint to

$$
Rc_{1!}Ri'_*c_{1Z}^!M
=Ri_*Rc_{1Z!}c_{1Z}^!M\xrightarrow{Ri_*\varepsilon_{c_{1Z}}}Ri_*M.
$$

The exceptional adjoint of the pushforward is thus a map
$\Theta Ri_*M\to Ri_*M$. After applying $i^*$ and the base change
identity $i^*\Theta Ri_*M\simeq Rc_{1Z!}c_{2Z}^*M$, it becomes the
exceptional adjoint of $u_{|Z}$. By
Lemma [lemma-lift-correspondence-invariant-decomposition] the same
holds for $\widehat u_Z$. Since $K_Z=Ri_*M$ and a map into $Ri_*M$ is
determined by its adjoint under $i^*\dashv Ri_*$, the two correspondences
agree.
