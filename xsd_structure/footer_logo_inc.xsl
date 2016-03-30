<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:from="rebelrunner_unformatted.xsd" 
    xmlns="rebelrunner.xsd" 
    >

    <xsl:template match="from:Footer" mode="footer_logo">
        <block name="FooterLogo">
            <xsl:apply-templates select="*" />
        </block>
    </xsl:template>

    <xsl:template match="from:list|from:list_item" >
        <xsl:apply-templates select="*" />
    </xsl:template>

    <xsl:template match="from:list_item/from:link" >
        <logo class="footer-menu__link" href="{ @href }" target="{ @target }">
            <xsl:value-of select="." />
        </logo>
    </xsl:template>

</xsl:stylesheet>
