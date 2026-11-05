+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--6"
order = 562013
+++
The comparisons are the adjoint transposes specified below.

We write
$\varepsilon_N:Rf_!f^!N\to N$ for the counit of
$Rf_!\dashv f^!$ (for $f=p$ this is (6.8)). The map (6.13) is the
transpose of the morphism

$$
Rf_!(f^*N\otimes^{\mathbf L}\omega_f)
\xrightarrow{\ \sim\ }
N\otimes^{\mathbf L}Rf_!\omega_f
\xrightarrow{1\otimes\varepsilon_{\Lambda_S}}N ,
$$

where the first arrow is the projection formula. By
Definition [definition-exceptional-base-change-finite], the map
(6.1) is the transpose, for $f'$, of the morphism
(6.2).

*(6.1) is an isomorphism.* For each type of chart,
under the explicit description of $f^!$ as a
twisted inverse image, (6.1) is the evident identification of
inverse images. For the projective line, the transpose of
(6.2) is the usual identification
$g'^*p^*N(1)[2]=p'^*g^*N(1)[2]$ of pullbacks. This holds because the unit
(6.7) and counit (6.8) commute with base change.
By restriction to the affine line and composition, the same holds for
affine space. For a separated étale map $u$, the transpose is again the
usual identification of inverse images. Indeed, the stalk of $u_!M$ at a
geometric point is the direct sum of the stalks of $M$ at the geometric
points over it. This description is compatible with base change, and under
it the counit $u_!u^*N\to N$ is the sum of the identity maps of the stalks
of $N$.

The cases combine, because base change for $Rf_!$ is compatible with
composition [Stacks, [0F7L](https://stacks.math.columbia.edu/tag/0F7L)] and the counit of a composite is the composite of
the counits. The open immersions $u$ and $v$ are étale. Substituting
these facts into (6.2), we see that the restriction of
(6.1) to $U\times_XX'$ is the composite of the étale and
affine-space cases just treated. Hence (6.1) is an
isomorphism on a cover of $X'$, and therefore it is an isomorphism.

*Source:* the proof of Proposition [proposition-exceptional-inverse-image-smooth-morphism].
