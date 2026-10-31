+++
id = "sk-rem-restriction-of-injectives-to-the-closed-fibre"
kind = "remark"
order = 205
tags = ["sketch"]
+++
1. A sheaf of $\mathbf F_\ell$-modules is a filtered colimit of
   constructible ones [Stacks, Tag 03SA](https://stacks.math.columbia.edu/tag/03SA), and cohomology commutes with filtered
   colimits [Stacks, Tag 03Q5](https://stacks.math.columbia.edu/tag/03Q5).
2. A constructible sheaf $G$ of $\mathbf F_\ell$-modules on
   $\mathbf P^1_{R,\acute{e}t}$ admits a monomorphism

$$
G\hookrightarrow
\bigoplus_{a=1}^N(h_a)_*\underline{M_a},
\qquad h_a:Y_a\to \mathbf P^1_R\ \text{finite and finitely presented},
\tag{4.8}
$$

with $M_a$ finite $\mathbf F_\ell$-modules [Stacks, Tag 09Z7](https://stacks.math.columbia.edu/tag/09Z7).
3. For a finite morphism $h:Y\to \mathbf P^1_R$ and an abelian sheaf
   $G$ on $Y_{\acute{e}t}$, we have

$$
R^qh_*G=0\quad(q>0),\qquad
i^*h_*G\xrightarrow{\sim}(h_0)_*i_Y^*G.
\tag{4.9}
$$

Here $h_0:Y_0=Y\times_{\mathbf P^1_R}\mathbf P^1_\kappa\to \mathbf P^1_\kappa$ and
$i_Y:Y_0\to Y$ are the base changes of $h$ and $i$, and the second
map is the underived base change map (4.2).
