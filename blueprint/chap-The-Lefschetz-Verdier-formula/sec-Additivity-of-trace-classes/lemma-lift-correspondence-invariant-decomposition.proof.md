+++
kind = "proof"
of = "lemma-lift-correspondence-invariant-decomposition"
order = 938
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-pro-etale-affines-form-basis", "proposition-construction-independence-rf-shriek"]
+++
By the hypothesis $c_1^{-1}(Z)\subset c_2^{-1}(Z)$, base change of
$Rc_{1!}$ along $i$, and the adjunction $i^*\dashv Ri_*$, we have

$$
i^*\Theta K_U=0,\qquad
R\operatorname{Hom}_X(\Theta K_U,K_Z)
\simeq R\operatorname{Hom}_Z(i^*\Theta K_U,i^*K)=0.
$$

The second vanishing is that of the whole mapping complex, including
all shifts. Hence the composite $\Theta K_U\to\Theta K\xrightarrow{\widehat u}K$
factors through $K_U\to K$, with a contractible space of choices. The
coherent cofibre of this factorization is a morphism of two-step
filtered objects

$$
\begin{array}{ccccc}
\Theta K_U&\longrightarrow&\Theta K&\longrightarrow&\Theta K_Z\\
\downarrow&&\downarrow \widehat u&&\downarrow\\
K_U&\longrightarrow&K&\longrightarrow&K_Z.
\end{array}
$$

Since this cofibre includes the homotopy, it is a morphism in the filtered derived
category, and its adjoint under the filtered adjunction
$Rc_{1!}\dashv c_1^!$ is the lift $\tilde u$. By base change, composition
and nilpotent invariance (which lets us use the reduced scheme $C_Z$),

$$
\Theta K_U\simeq j_!Rc_{1U!}c_{2U}^*j^*K,
\qquad i^*\Theta K\simeq Rc_{1Z!}c_{2Z}^*i^*K.
$$

Applying $i^*$ to the right-hand square and using $i^*\Theta K_U=0$, so
that $i^*\Theta K\simeq i^*\Theta K_Z$, we obtain the formula for
$\widehat u_Z$ restricted to $Z$.
