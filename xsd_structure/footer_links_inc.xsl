<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:from="rebelrunner_unformatted.xsd" 
    xmlns="rebelrunner.xsd" 
    >

    <xsl:template match="from:Footer" mode="footer_links">
        <block name="FooterLinks">
            <xsl:apply-templates select="*" mode="fl"/>
        </block>
    </xsl:template>

    <xsl:template match="*" mode="fl">
        <xsl:element name="{name()}">
            <xsl:apply-templates select="@*|node()" mode="fl"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="@*" mode="fl">
        <xsl:copy/>
    </xsl:template>

    <xsl:template match="from:list|from:list_item" mode="fl">
        <xsl:apply-templates select="*" mode="fl"/>
    </xsl:template>

    <xsl:template match="from:list_item/from:link" mode="fl">
        <a class="footer-menu__link" href="{ @href }" target="{ @target }">
            <xsl:value-of select="." />
        </a>
    </xsl:template>

</xsl:stylesheet>
